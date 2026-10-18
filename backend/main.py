
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import hashlib
import secrets
import os

from database import get_connection, create_database
from ai_engine import generate_quiz_questions


# =========================================================
# APP
# =========================================================

app = FastAPI(
    title="AI Quiz Battle API",
    version="2.0.0"
)


# =========================================================
# CORS CONFIGURATION
# =========================================================

# Add your actual deployed frontend URL to FRONTEND_URL
FRONTEND_URL = os.getenv(
    "FRONTEND_URL",
   "https://ai-quiz-battle-llmz.onrender.com",
).strip().rstrip("/")

allowed_origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

# Don't add the placeholder URL to the allowed origins.
if (
    FRONTEND_URL
    and "YOUR-FRONTEND-NAME" not in FRONTEND_URL
):
    allowed_origins.append(FRONTEND_URL)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================================================
# DATABASE
# =========================================================

create_database()


# =========================================================
# MODELS
# =========================================================

class StudentRegister(BaseModel):
    name: str
    email: str
    password: str


class StudentLogin(BaseModel):
    email: str
    password: str


class QuizRequest(BaseModel):
    category: str = "Python"
    difficulty: str = "Medium"
    count: int = 20


class QuizResult(BaseModel):
    username: str
    score: int
    xp: int
    streak: int


# =========================================================
# PASSWORD FUNCTIONS
# =========================================================

def hash_password(
    password: str,
    salt: Optional[str] = None
) -> str:
    if salt is None:
        salt = secrets.token_hex(16)

    hashed = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt.encode("utf-8"),
        100000
    )

    return f"{salt}${hashed.hex()}"


def verify_password(
    password: str,
    stored_password: str
) -> bool:
    try:
        salt, stored_hash = stored_password.split("$", 1)

        hashed = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt.encode("utf-8"),
            100000
        )

        return secrets.compare_digest(
            hashed.hex(),
            stored_hash
        )

    except (ValueError, AttributeError):
        return False


# =========================================================
# ROOT
# =========================================================

@app.get("/")
def root():
    return {
        "message": "AI Quiz Battle API is running",
        "status": "success"
    }


# =========================================================
# HEALTH CHECK
# =========================================================

@app.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "message": "AI Quiz Battle backend is working."
    }


# =========================================================
# REGISTER
# =========================================================

@app.post("/api/register")
def register_student(student: StudentRegister):
    name = student.name.strip()
    email = student.email.strip().lower()
    password = student.password

    if not name:
        raise HTTPException(
            status_code=400,
            detail="Name is required."
        )

    if not email:
        raise HTTPException(
            status_code=400,
            detail="Email is required."
        )

    if len(password) < 6:
        raise HTTPException(
            status_code=400,
            detail="Password must be at least 6 characters."
        )

    connection = get_connection()

    try:
        existing_student = connection.execute(
            """
            SELECT id
            FROM students
            WHERE email = ?
            """,
            (email,)
        ).fetchone()

        if existing_student:
            raise HTTPException(
                status_code=400,
                detail="An account with this email already exists."
            )

        hashed_password = hash_password(password)

        cursor = connection.execute(
            """
            INSERT INTO students (name, email, password)
            VALUES (?, ?, ?)
            """,
            (name, email, hashed_password)
        )

        connection.commit()
        student_id = cursor.lastrowid

        return {
            "message": "Registration successful.",
            "student": {
                "id": student_id,
                "name": name,
                "email": email
            }
        }

    finally:
        connection.close()


# =========================================================
# LOGIN
# =========================================================

@app.post("/api/login")
def login_student(student: StudentLogin):
    email = student.email.strip().lower()

    connection = get_connection()

    try:
        existing_student = connection.execute(
            """
            SELECT id, name, email, password
            FROM students
            WHERE email = ?
            """,
            (email,)
        ).fetchone()

    finally:
        connection.close()

    if not existing_student:
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password."
        )

    if not verify_password(
        student.password,
        existing_student["password"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password."
        )

    return {
        "message": "Login successful.",
        "student": {
            "id": existing_student["id"],
            "name": existing_student["name"],
            "email": existing_student["email"]
        }
    }


# =========================================================
# GET ALL STUDENTS
# =========================================================

@app.get("/api/students")
def get_students():
    connection = get_connection()

    try:
        students = connection.execute(
            """
            SELECT id, name, email, created_at
            FROM students
            ORDER BY id DESC
            """
        ).fetchall()

        return [
            {
                "id": student["id"],
                "name": student["name"],
                "email": student["email"],
                "created_at": student["created_at"]
            }
            for student in students
        ]

    finally:
        connection.close()


# =========================================================
# GENERATE QUIZ
# =========================================================

@app.post("/api/generate-quiz")
def generate_quiz(request: QuizRequest):
    category = request.category.strip()
    difficulty = request.difficulty.strip().title()

    if not category:
        raise HTTPException(
            status_code=400,
            detail="Category is required."
        )

    count = request.count

    if count not in [10, 15, 20]:
        count = 20

    allowed_difficulties = [
        "Easy",
        "Medium",
        "Hard"
    ]

    if difficulty not in allowed_difficulties:
        difficulty = "Medium"

    try:
        questions = generate_quiz_questions(
            category=category,
            difficulty=difficulty,
            count=count
        )

        if not questions:
            raise HTTPException(
                status_code=500,
                detail="Unable to generate quiz questions."
            )

        return {
            "category": category,
            "difficulty": difficulty,
            "count": len(questions),
            "questions": questions
        }

    except HTTPException:
        raise

    except Exception as error:
        print("Quiz generation error:", error)

        raise HTTPException(
            status_code=500,
            detail="Failed to generate quiz."
        )


# =========================================================
# SAVE QUIZ RESULT
# =========================================================

@app.post("/api/results")
def save_result(result: QuizResult):
    username = result.username.strip()

    if not username:
        raise HTTPException(
            status_code=400,
            detail="Username is required."
        )

    connection = get_connection()

    try:
        cursor = connection.execute(
            """
            INSERT INTO quiz_results
            (username, score, xp, streak)
            VALUES (?, ?, ?, ?)
            """,
            (
                username,
                result.score,
                result.xp,
                result.streak
            )
        )

        connection.commit()

        return {
            "message": "Result saved successfully.",
            "result_id": cursor.lastrowid,
            "username": username,
            "score": result.score,
            "xp": result.xp,
            "streak": result.streak
        }

    finally:
        connection.close()


# =========================================================
# LEADERBOARD
# =========================================================

@app.get("/api/leaderboard")
def get_leaderboard():
    connection = get_connection()

    try:
        leaderboard = connection.execute(
            """
            SELECT
                username,
                MAX(score) AS best_score,
                SUM(xp) AS total_xp,
                MAX(streak) AS best_streak,
                COUNT(*) AS quizzes_completed
            FROM quiz_results
            GROUP BY username
            ORDER BY total_xp DESC, best_score DESC
            LIMIT 50
            """
        ).fetchall()

        return [
            {
                "rank": index + 1,
                "username": row["username"],
                "score": row["best_score"] or 0,
                "best_score": row["best_score"] or 0,
                "xp": row["total_xp"] or 0,
                "total_xp": row["total_xp"] or 0,
                "streak": row["best_streak"] or 0,
                "best_streak": row["best_streak"] or 0,
                "quizzes_completed": row["quizzes_completed"] or 0
            }
            for index, row in enumerate(leaderboard)
        ]

    finally:
        connection.close()


# =========================================================
# STUDENT STATISTICS
# =========================================================

@app.get("/api/student-stats/{username}")
def get_student_stats(username: str):
    username = username.strip()

    connection = get_connection()

    try:
        results = connection.execute(
            """
            SELECT score, xp, streak
            FROM quiz_results
            WHERE username = ?
            ORDER BY id DESC
            """,
            (username,)
        ).fetchall()

    finally:
        connection.close()

    if not results:
        return {
            "username": username,
            "quizzes_completed": 0,
            "best_score": 0,
            "total_xp": 0,
            "best_streak": 0,
            "average_score": 0,
            "recent_results": []
        }

    scores = [row["score"] for row in results]
    xp_values = [row["xp"] for row in results]
    streaks = [row["streak"] for row in results]

    quizzes_completed = len(results)

    return {
        "username": username,
        "quizzes_completed": quizzes_completed,
        "best_score": max(scores),
        "total_xp": sum(xp_values),
        "best_streak": max(streaks),
        "average_score": round(
            sum(scores) / quizzes_completed,
            1
        ),
        "recent_results": [
            {
                "score": row["score"],
                "xp": row["xp"],
                "streak": row["streak"]
            }
            for row in results[:5]
        ]
    }
