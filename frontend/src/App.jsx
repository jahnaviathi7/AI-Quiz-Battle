import React, { useEffect, useMemo, useState } from "react";
import "./style.css";

const API = "https://ai-quiz-battle-backend.onrender.com";

const CATEGORIES = [
  "Python",
  "Java",
  "C Programming",
  "C++",
  "JavaScript",
  "React",
  "HTML & CSS",
  "Data Structures",
  "Algorithms",
  "DBMS",
  "Operating Systems",
  "Computer Networks",
  "Cloud Computing",
  "Machine Learning",
  "Artificial Intelligence",
  "Cyber Security",
];

const DIFFICULTIES = ["Easy", "Medium", "Hard"];
const QUESTION_COUNTS = [10, 15, 20];

function App() {
  const [student, setStudent] = useState(() => {
    try {
      return JSON.parse(localStorage.getItem("quiz_student") || "null");
    } catch {
      return null;
    }
  });

  const [page, setPage] = useState("home");
  const [authMode, setAuthMode] = useState("login");

  const [authName, setAuthName] = useState("");
  const [authEmail, setAuthEmail] = useState("");
  const [authPassword, setAuthPassword] = useState("");
  const [authError, setAuthError] = useState("");
  const [authLoading, setAuthLoading] = useState(false);

  const [category, setCategory] = useState("Python");
  const [difficulty, setDifficulty] = useState("Medium");
  const [questionCount, setQuestionCount] = useState(20);

  const [questions, setQuestions] = useState([]);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [answered, setAnswered] = useState(false);

  const [timeLeft, setTimeLeft] = useState(30);
  const [score, setScore] = useState(0);
  const [xp, setXp] = useState(0);
  const [streak, setStreak] = useState(0);
  const [bestStreak, setBestStreak] = useState(0);

  const [studentStats, setStudentStats] = useState({
    username: "",
    quizzes_completed: 0,
    best_score: 0,
    total_xp: 0,
    best_streak: 0,
    average_score: 0,
    recent_results: [],
  });

  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");

  const question = questions[currentQuestion];

  const progress = useMemo(() => {
    if (!questions.length) return 0;

    return Math.round(
      ((currentQuestion + 1) / questions.length) * 100
    );
  }, [currentQuestion, questions.length]);

  useEffect(() => {
    if (student) {
      fetchStudentStats();
      fetchLeaderboard();
    }
  }, [student]);

  useEffect(() => {
    if (
      page !== "quiz" ||
      answered ||
      !questions.length
    ) {
      return;
    }

    if (timeLeft <= 0) {
      handleAnswer(null);
      return;
    }

    const timer = setInterval(() => {
      setTimeLeft((previous) => previous - 1);
    }, 1000);

    return () => clearInterval(timer);
  }, [
    page,
    answered,
    timeLeft,
    questions.length,
  ]);

  const fetchStudentStats = async () => {
    if (!student?.name) return;

    try {
      const response = await fetch(
        `${API}/api/student-stats/${encodeURIComponent(
          student.name
        )}`
      );

      if (!response.ok) return;

      const data = await response.json();

      setStudentStats({
        username: data.username || student.name,
        quizzes_completed: Number(
          data.quizzes_completed || 0
        ),
        best_score: Number(data.best_score || 0),
        total_xp: Number(data.total_xp || 0),
        best_streak: Number(data.best_streak || 0),
        average_score: Number(
          data.average_score || 0
        ),
        recent_results:
          data.recent_results || [],
      });
    } catch (error) {
      console.error(
        "Failed to fetch student stats:",
        error
      );
    }
  };

  const fetchLeaderboard = async () => {
    try {
      const response = await fetch(
        `${API}/api/leaderboard`
      );

      if (!response.ok) return;

      const data = await response.json();

      setLeaderboard(
        Array.isArray(data)
          ? data
          : data.results || []
      );
    } catch (error) {
      console.error(
        "Failed to fetch leaderboard:",
        error
      );
    }
  };

  const handleAuth = async (event) => {
    event.preventDefault();

    setAuthError("");

    if (
      !authEmail.trim() ||
      !authPassword.trim()
    ) {
      setAuthError(
        "Please enter your email and password."
      );
      return;
    }

    if (
      authMode === "register" &&
      !authName.trim()
    ) {
      setAuthError("Please enter your name.");
      return;
    }

    if (
      authMode === "register" &&
      authPassword.length < 6
    ) {
      setAuthError(
        "Password must contain at least 6 characters."
      );
      return;
    }

    setAuthLoading(true);

    try {
      const endpoint =
        authMode === "register"
          ? `${API}/api/register`
          : `${API}/api/login`;

      const body =
        authMode === "register"
          ? {
              name: authName.trim(),
              email: authEmail
                .trim()
                .toLowerCase(),
              password: authPassword,
            }
          : {
              email: authEmail
                .trim()
                .toLowerCase(),
              password: authPassword,
            };

      const response = await fetch(endpoint, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(body),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail ||
            "Authentication failed."
        );
      }

      const loggedStudent = data.student
        ? {
            id: data.student.id,
            name: data.student.name,
            email: data.student.email,
          }
        : {
            id: data.id,
            name: data.name,
            email: data.email,
          };

      localStorage.setItem(
        "quiz_student",
        JSON.stringify(loggedStudent)
      );

      setStudent(loggedStudent);

      setAuthName("");
      setAuthEmail("");
      setAuthPassword("");
      setAuthError("");
      setPage("home");
    } catch (error) {
      setAuthError(
        error.message ||
          "Something went wrong."
      );
    } finally {
      setAuthLoading(false);
    }
  };

  const logout = () => {
    localStorage.removeItem("quiz_student");

    setStudent(null);
    setPage("home");
    setQuestions([]);
    setCurrentQuestion(0);
    setScore(0);
    setXp(0);
    setStreak(0);
    setBestStreak(0);

    setStudentStats({
      username: "",
      quizzes_completed: 0,
      best_score: 0,
      total_xp: 0,
      best_streak: 0,
      average_score: 0,
      recent_results: [],
    });
  };

  const startQuiz = async () => {
    setLoading(true);
    setMessage("");

    try {
      const response = await fetch(
        `${API}/api/generate-quiz`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            category,
            difficulty,
            count: questionCount,
          }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail ||
            "Unable to generate quiz."
        );
      }

      const generatedQuestions =
        data.questions ||
        data.quiz ||
        data ||
        [];

      if (
        !Array.isArray(
          generatedQuestions
        ) ||
        generatedQuestions.length === 0
      ) {
        throw new Error(
          "No questions were generated."
        );
      }

      setQuestions(generatedQuestions);
      setCurrentQuestion(0);
      setSelectedAnswer(null);
      setAnswered(false);
      setTimeLeft(30);
      setScore(0);
      setXp(0);
      setStreak(0);
      setBestStreak(0);
      setPage("quiz");
    } catch (error) {
      console.error(error);

      setMessage(
        error.message ||
          "Unable to start quiz."
      );
    } finally {
      setLoading(false);
    }
  };

  const getCorrectAnswer = (current) => {
    if (!current) return "";

    return (
      current.correct_answer ??
      current.correctAnswer ??
      current.answer ??
      current.correct ??
      ""
    );
  };

  const getQuestionText = (current) => {
    if (!current) return "";

    return (
      current.question ??
      current.question_text ??
      current.text ??
      ""
    );
  };

  const getOptions = (current) => {
    if (!current) return [];

    if (Array.isArray(current.options)) {
      return current.options;
    }

    if (Array.isArray(current.answers)) {
      return current.answers;
    }

    return [];
  };

  const isCorrectAnswer = (
    selected,
    correct
  ) => {
    if (
      selected === null ||
      selected === undefined
    ) {
      return false;
    }

    const normalize = (value) =>
      String(value ?? "")
        .trim()
        .toLowerCase();

    return (
      normalize(selected) ===
      normalize(correct)
    );
  };

  const handleAnswer = (answer) => {
    if (answered || !question) return;

    const correctAnswer =
      getCorrectAnswer(question);

    const correct = isCorrectAnswer(
      answer,
      correctAnswer
    );

    setSelectedAnswer(answer);
    setAnswered(true);

    if (correct) {
      const newStreak = streak + 1;
      const points =
        10 + Math.min(timeLeft, 30);

      setScore(
        (previous) => previous + points
      );

      setXp(
        (previous) =>
          previous +
          20 +
          newStreak * 5
      );

      setStreak(newStreak);

      setBestStreak(
        (previous) =>
          Math.max(
            previous,
            newStreak
          )
      );
    } else {
      setStreak(0);
    }
  };

  const finishQuiz = async () => {
    const finalScore = score;
    const finalXp = xp;
    const finalStreak = Math.max(
      bestStreak,
      streak
    );

    try {
      const response = await fetch(
        `${API}/api/results`,
        {
          method: "POST",
          headers: {
            "Content-Type":
              "application/json",
          },
          body: JSON.stringify({
            username: student.name,
            score: finalScore,
            xp: finalXp,
            streak: finalStreak,
          }),
        }
      );

      if (!response.ok) {
        const data =
          await response
            .json()
            .catch(() => ({}));

        throw new Error(
          data.detail ||
            "Failed to save quiz result."
        );
      }

      await fetchStudentStats();
      await fetchLeaderboard();

      setPage("result");
    } catch (error) {
      console.error(
        "Failed to save quiz result:",
        error
      );

      setMessage(
        error.message ||
          "Failed to save quiz result."
      );
    }
  };

  const nextQuestion = async () => {
    if (
      currentQuestion <
      questions.length - 1
    ) {
      setCurrentQuestion(
        (previous) =>
          previous + 1
      );

      setSelectedAnswer(null);
      setAnswered(false);
      setTimeLeft(30);

      return;
    }

    await finishQuiz();
  };

  const goHome = async () => {
    await fetchStudentStats();
    await fetchLeaderboard();

    setPage("home");
  };

  const getInitials = (name) => {
    if (!name) return "?";

    return name
      .split(" ")
      .map((part) => part[0])
      .join("")
      .slice(0, 2)
      .toUpperCase();
  };

  if (!student) {
    return (
      <div className="auth-page">
        <div className="auth-background">
          <div className="auth-orb orb-one"></div>
          <div className="auth-orb orb-two"></div>
          <div className="auth-orb orb-three"></div>
        </div>

        <div className="auth-card">
          <div className="auth-logo">
            <span className="brand-icon">
              ⚡
            </span>
          </div>

          <h1 className="auth-heading">
            AI Quiz Battle
          </h1>

          <p className="auth-subtitle">
            Test your CSE knowledge.
            Compete. Improve.
          </p>

          <div className="auth-tabs">
            <button
              className={`auth-tab ${
                authMode === "login"
                  ? "active"
                  : ""
              }`}
              onClick={() => {
                setAuthMode("login");
                setAuthError("");
              }}
            >
              Login
            </button>

            <button
              className={`auth-tab ${
                authMode === "register"
                  ? "active"
                  : ""
              }`}
              onClick={() => {
                setAuthMode("register");
                setAuthError("");
              }}
            >
              Register
            </button>
          </div>

          <form onSubmit={handleAuth}>
            {authMode ===
              "register" && (
              <div className="input-group">
                <label>Full Name</label>

                <input
                  type="text"
                  value={authName}
                  onChange={(event) =>
                    setAuthName(
                      event.target.value
                    )
                  }
                  placeholder="Enter your name"
                />
              </div>
            )}

            <div className="input-group">
              <label>
                Email Address
              </label>

              <input
                type="email"
                value={authEmail}
                onChange={(event) =>
                  setAuthEmail(
                    event.target.value
                  )
                }
                placeholder="Enter your email"
              />
            </div>

            <div className="input-group">
              <label>Password</label>

              <input
                type="password"
                value={authPassword}
                onChange={(event) =>
                  setAuthPassword(
                    event.target.value
                  )
                }
                placeholder="Enter your password"
              />
            </div>

            {authError && (
              <div className="auth-error">
                {authError}
              </div>
            )}

            <button
              type="submit"
              className="primary-auth-button"
              disabled={authLoading}
            >
              {authLoading
                ? "Please wait..."
                : authMode === "login"
                ? "Login"
                : "Create Account"}
            </button>
          </form>

          <div className="auth-footer">
            AI-Powered Interactive Quiz
            Platform
          </div>
        </div>
      </div>
    );
  }

  if (page === "quiz") {
    const options =
      getOptions(question);

    const correctAnswer =
      getCorrectAnswer(question);

    return (
      <div className="app">
        <nav className="navbar">
          <div
            className="brand"
            onClick={goHome}
            style={{
              cursor: "pointer",
            }}
          >
            <span className="brand-icon">
              ⚡
            </span>

            <div>
              <div className="brand-title">
                AI Quiz Battle
              </div>

              <div className="brand-subtitle">
                CSE Challenge
              </div>
            </div>
          </div>

          <div className="student-menu">
            <div className="student-avatar">
              {getInitials(
                student.name
              )}
            </div>

            <div className="student-info">
              <strong>
                {student.name}
              </strong>

              <span>
                {student.email}
              </span>
            </div>

            <button
              className="logout-button"
              onClick={logout}
            >
              Logout
            </button>
          </div>
        </nav>

        <main className="quiz-page">
          <div className="quiz-top">
            <div className="quiz-stats">
              <div className="quiz-stat">
                <span>Score</span>
                <strong>
                  {score}
                </strong>
              </div>

              <div className="quiz-stat">
                <span>XP</span>
                <strong>
                  {xp}
                </strong>
              </div>

              <div className="quiz-stat">
                <span>Streak</span>
                <strong>
                  🔥 {streak}
                </strong>
              </div>

              <div className="timer">
                ⏱ {timeLeft}s
              </div>
            </div>
          </div>

          <div className="progress-container">
            <div className="progress-info">
              <span>
                Question{" "}
                {currentQuestion + 1}{" "}
                of {questions.length}
              </span>

              <span>
                {progress}%
              </span>
            </div>

            <div className="progress-bar">
              <div
                className="progress-fill"
                style={{
                  width: `${progress}%`,
                }}
              ></div>
            </div>
          </div>

          <div className="question-card">
            <div className="question-number">
              {category} •{" "}
              {difficulty}
            </div>

            <h2>
              {getQuestionText(
                question
              )}
            </h2>

            <div className="answers-grid">
              {options.map(
                (option, index) => {
                  const optionLetter =
                    String.fromCharCode(
                      65 + index
                    );

                  let answerClass =
                    "answer-option";

                  if (answered) {
                    if (
                      isCorrectAnswer(
                        option,
                        correctAnswer
                      )
                    ) {
                      answerClass +=
                        " correct";
                    } else if (
                      selectedAnswer !==
                        null &&
                      isCorrectAnswer(
                        option,
                        selectedAnswer
                      )
                    ) {
                      answerClass +=
                        " wrong";
                    }
                  }

                  return (
                    <button
                      key={`${index}-${String(
                        option
                      )}`}
                      className={
                        answerClass
                      }
                      onClick={() =>
                        handleAnswer(
                          option
                        )
                      }
                      disabled={
                        answered
                      }
                    >
                      <span className="option-letter">
                        {optionLetter}
                      </span>

                      <span className="option-text">
                        {option}
                      </span>
                    </button>
                  );
                }
              )}
            </div>

            {answered && (
              <div
                className={`answer-feedback ${
                  isCorrectAnswer(
                    selectedAnswer,
                    correctAnswer
                  )
                    ? "feedback-correct"
                    : "feedback-wrong"
                }`}
              >
                {isCorrectAnswer(
                  selectedAnswer,
                  correctAnswer
                )
                  ? "✓ Correct answer!"
                  : `✗ Incorrect. Correct answer: ${correctAnswer}`}
              </div>
            )}

            <div className="question-footer">
              <button
                className="next-button"
                onClick={
                  nextQuestion
                }
                disabled={!answered}
              >
                {currentQuestion ===
                questions.length - 1
                  ? "Finish Quiz"
                  : "Next Question →"}
              </button>
            </div>
          </div>
        </main>
      </div>
    );
  }

  if (page === "result") {
    const percentage =
      questions.length > 0
        ? Math.round(
            (score /
              (questions.length *
                40)) *
              100
          )
        : 0;

    return (
      <div className="app">
        <nav className="navbar">
          <div
            className="brand"
            onClick={goHome}
            style={{
              cursor: "pointer",
            }}
          >
            <span className="brand-icon">
              ⚡
            </span>

            <div>
              <div className="brand-title">
                AI Quiz Battle
              </div>

              <div className="brand-subtitle">
                CSE Challenge
              </div>
            </div>
          </div>

          <div className="student-menu">
            <div className="student-avatar">
              {getInitials(
                student.name
              )}
            </div>

            <div className="student-info">
              <strong>
                {student.name}
              </strong>

              <span>
                {student.email}
              </span>
            </div>

            <button
              className="logout-button"
              onClick={logout}
            >
              Logout
            </button>
          </div>
        </nav>

        <main className="result-page">
          <div className="result-hero">
            <div className="result-trophy">
              🏆
            </div>

            <h1>
              Quiz Complete!
            </h1>

            <p>
              Great job,{" "}
              {student.name}! Here is
              your performance.
            </p>
          </div>

          <div className="result-score-card">
            <span>
              Your Score
            </span>

            <div className="main-score">
              {score}
            </div>

            <strong>
              {percentage}% Performance
            </strong>
          </div>

          <div className="result-stats">
            <div className="quiz-stat">
              <span>
                XP Earned
              </span>

              <strong>
                {xp}
              </strong>
            </div>

            <div className="quiz-stat">
              <span>
                Best Streak
              </span>

              <strong>
                🔥 {bestStreak}
              </strong>
            </div>

            <div className="quiz-stat">
              <span>
                Questions
              </span>

              <strong>
                {questions.length}
              </strong>
            </div>
          </div>

          <div className="result-actions">
            <button
              className="result-primary"
              onClick={goHome}
            >
              Back to Dashboard
            </button>

            <button
              className="result-secondary"
              onClick={() => {
                setPage("home");

                setTimeout(
                  () => startQuiz(),
                  0
                );
              }}
            >
              Play Again
            </button>
          </div>
        </main>
      </div>
    );
  }

  if (page === "leaderboard") {
    return (
      <div className="app">
        <nav className="navbar">
          <div
            className="brand"
            onClick={goHome}
            style={{
              cursor: "pointer",
            }}
          >
            <span className="brand-icon">
              ⚡
            </span>

            <div>
              <div className="brand-title">
                AI Quiz Battle
              </div>

              <div className="brand-subtitle">
                CSE Challenge
              </div>
            </div>
          </div>

          <div className="student-menu">
            <div className="student-avatar">
              {getInitials(
                student.name
              )}
            </div>

            <div className="student-info">
              <strong>
                {student.name}
              </strong>

              <span>
                {student.email}
              </span>
            </div>

            <button
              className="logout-button"
              onClick={logout}
            >
              Logout
            </button>
          </div>
        </nav>

        <main className="leaderboard-page">
          <div className="leaderboard-header">
            <span className="section-label">
              GLOBAL RANKING
            </span>

            <h1 className="section-heading">
              Leaderboard
            </h1>

            <p>
              See how you compare with
              other students.
            </p>
          </div>

          <div className="leaderboard-card">
            <div className="leaderboard-table-header">
              <span>Rank</span>
              <span>Student</span>
              <span>Score</span>
              <span>XP</span>
              <span>Streak</span>
            </div>

            {leaderboard.length ===
            0 ? (
              <div className="leaderboard-empty">
                No quiz results yet.
                Complete a quiz to
                appear here.
              </div>
            ) : (
              leaderboard.map(
                (item, index) => {
                  const name =
                    item.username ||
                    item.name ||
                    "Student";

                  return (
                    <div
                      className="leaderboard-row"
                      key={`${name}-${index}`}
                    >
                      <span>
                        #{index + 1}
                      </span>

                      <div className="leader-student">
                        <div className="leader-avatar">
                          {getInitials(
                            name
                          )}
                        </div>

                        <strong>
                          {name}
                        </strong>
                      </div>

                      <span>
                        {item.score ??
                          0}
                      </span>

                      <span>
                        {item.xp ??
                          0}
                      </span>

                      <span>
                        🔥{" "}
                        {item.streak ??
                          0}
                      </span>
                    </div>
                  );
                }
              )
            )}
          </div>
        </main>

        <footer className="footer">
          AI Quiz Battle • Built
          for CSE Students
        </footer>
      </div>
    );
  }

  return (
    <div className="app">
      <nav className="navbar">
        <div className="brand">
          <span className="brand-icon">
            ⚡
          </span>

          <div>
            <div className="brand-title">
              AI Quiz Battle
            </div>

            <div className="brand-subtitle">
              CSE Challenge
            </div>
          </div>
        </div>

        <div className="nav-links">
          <button
            className="nav-link active"
            onClick={goHome}
          >
            Dashboard
          </button>

          <button
            className="nav-link"
            onClick={async () => {
              await fetchLeaderboard();
              setPage(
                "leaderboard"
              );
            }}
          >
            Leaderboard
          </button>
        </div>

        <div className="student-menu">
          <div className="student-avatar">
            {getInitials(
              student.name
            )}
          </div>

          <div className="student-info">
            <strong>
              {student.name}
            </strong>

            <span>
              {student.email}
            </span>
          </div>

          <button
            className="logout-button"
            onClick={logout}
          >
            Logout
          </button>
        </div>
      </nav>

      <main className="home-page">
        <section className="hero-section">
          <div className="hero-content">
            <span className="hero-badge">
              ✨ AI-POWERED LEARNING
            </span>

            <h1>
              Challenge your
              <br />
              <span>
                coding knowledge.
              </span>
            </h1>

            <p>
              Generate intelligent CSE
              quizzes, build your
              streak, earn XP and
              compete with other
              students.
            </p>

            <div className="hero-buttons">
              <button
                className="hero-primary"
                onClick={() => {
                  document
                    .querySelector(
                      ".quiz-setup-section"
                    )
                    ?.scrollIntoView({
                      behavior:
                        "smooth",
                    });
                }}
              >
                Start a Quiz →
              </button>

              <button
                className="hero-secondary"
                onClick={async () => {
                  await fetchLeaderboard();
                  setPage(
                    "leaderboard"
                  );
                }}
              >
                View Leaderboard
              </button>
            </div>
          </div>

          <div className="hero-visual">
            <div className="quiz-orb">
              <div className="orb-inner">
                <span>AI</span>
                <small>
                  QUIZ
                </small>
              </div>
            </div>

            <div className="floating-card card-one">
              <span>
                🔥 Best Streak
              </span>

              <strong>
                {studentStats.best_streak ||
                  0}
              </strong>
            </div>

            <div className="floating-card card-two">
              <span>
                ⚡ Total XP
              </span>

              <strong>
                {studentStats.total_xp ||
                  0}
              </strong>
            </div>
          </div>
        </section>

        <section className="quiz-setup-section">
          <span className="section-label">
            QUIZ CONFIGURATION
          </span>

          <h2 className="section-heading">
            Build your challenge
          </h2>

          <div className="setup-card">
            <div className="setup-field">
              <label>
                Category
              </label>

              <select
                value={category}
                onChange={(event) =>
                  setCategory(
                    event.target.value
                  )
                }
              >
                {CATEGORIES.map(
                  (item) => (
                    <option
                      key={item}
                      value={item}
                    >
                      {item}
                    </option>
                  )
                )}
              </select>
            </div>

            <div className="setup-field">
              <label>
                Difficulty
              </label>

              <div className="difficulty-buttons">
                {DIFFICULTIES.map(
                  (item) => (
                    <button
                      key={item}
                      className={
                        difficulty ===
                        item
                          ? "selected"
                          : ""
                      }
                      onClick={() =>
                        setDifficulty(
                          item
                        )
                      }
                    >
                      {item}
                    </button>
                  )
                )}
              </div>
            </div>

            <div className="setup-field">
              <label>
                Questions
              </label>

              <div className="question-count-buttons">
                {QUESTION_COUNTS.map(
                  (count) => (
                    <button
                      key={count}
                      className={
                        questionCount ===
                        count
                          ? "selected"
                          : ""
                      }
                      onClick={() =>
                        setQuestionCount(
                          count
                        )
                      }
                    >
                      {count}
                    </button>
                  )
                )}
              </div>
            </div>

            {message && (
              <div className="auth-error">
                {message}
              </div>
            )}

            <button
              className="start-quiz-button"
              onClick={startQuiz}
              disabled={loading}
            >
              {loading
                ? "Generating Quiz..."
                : "Start Quiz →"}
            </button>
          </div>
        </section>

        <section className="feature-strip">
          <div className="feature-item">
            <span>🎯</span>

            <div>
              <strong>
                {studentStats.quizzes_completed ||
                  0}
              </strong>

              <small>
                Quizzes Completed
              </small>
            </div>
          </div>

          <div className="feature-item">
            <span>🏆</span>

            <div>
              <strong>
                {studentStats.best_score ||
                  0}
              </strong>

              <small>
                Best Score
              </small>
            </div>
          </div>

          <div className="feature-item">
            <span>⚡</span>

            <div>
              <strong>
                {studentStats.total_xp ||
                  0}
              </strong>

              <small>
                Total XP
              </small>
            </div>
          </div>

          <div className="feature-item">
            <span>📊</span>

            <div>
              <strong>
                {studentStats.average_score ||
                  0}
              </strong>

              <small>
                Average Score
              </small>
            </div>
          </div>
        </section>
      </main>

      <footer className="footer">
        AI Quiz Battle • Built
        for CSE Students
      </footer>
    </div>
  );
}

export default App;