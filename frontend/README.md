# 🎯 AI Quiz Battle

### Test Your CSE Knowledge. Compete. Improve.

AI Quiz Battle is a full-stack web application designed to help students practise Computer Science Engineering (CSE) topics through interactive, timed quizzes. It includes quiz generation, automatic scoring, XP and streak tracking, student statistics, and a leaderboard.

## 🌐 Project Links

- **Live Website:** https://ai-quiz-battle-llmz.onrender.com/
- **GitHub Repository:** https://github.com/jahnaviathi7/AI-Quiz-Battle
- **Backend API:** https://ai-quiz-battle-backend.onrender.com
- **API Documentation:** https://ai-quiz-battle-backend.onrender.com/docs

## ✨ Features

- 👤 Student registration and login
- 🧠 Category-based CSE quizzes
- 🎚️ Difficulty selection
- ⏱️ Timed quiz sessions
- 📊 Automatic score calculation
- ⭐ XP and streak tracking
- 💾 Saved quiz results
- 📈 Student performance statistics
- 🏆 Leaderboard
- 🌍 Online deployment

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| React | Interactive frontend |
| Vite | Frontend development and build |
| JavaScript | Application logic |
| HTML5 and CSS3 | Structure and styling |
| Python | Backend logic |
| FastAPI | REST API development |
| Pydantic | Request validation |
| SQLite | Data storage |
| Git and GitHub | Version control |
| Render | Deployment and hosting |

## 🏗️ System Architecture

```text
              STUDENT
                 |
                 v
          React + Vite UI
                 |
            HTTP / JSON
                 |
                 v
           FastAPI Backend
            /          \
           v            v
     Quiz Engine    SQLite Database
           \            /
            v          v
         Results and Statistics
                 |
                 v
          Leaderboard and UI
```

## ⚙️ How It Works

1. Students register or log in.
2. They select a quiz category and difficulty.
3. The frontend requests quiz questions from the backend.
4. The quiz engine generates or supplies the questions.
5. Students answer questions within the given time.
6. The application calculates and saves quiz results.
7. Students can view their scores, XP, statistics, and leaderboard position.

## 🚀 Run Locally

### Prerequisites

- Python 3
- Node.js and npm
- Git

### 1. Clone the repository

```bash
git clone https://github.com/jahnaviathi7/AI-Quiz-Battle.git
cd AI-Quiz-Battle
```

### 2. Start the backend

Open a terminal:

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend API: http://127.0.0.1:8000

API documentation: http://127.0.0.1:8000/docs

### 3. Start the frontend

Open a second terminal from the project root:

```bash
cd frontend
npm install
npm run dev
```

Open the local URL displayed in the terminal by Vite.

**Note:** Make sure the frontend API configuration points to your local backend when running locally.

## 🧪 Testing Checklist

- [ ] Register a new account
- [ ] Log in with valid credentials
- [ ] Test invalid login details
- [ ] Generate quizzes in different categories
- [ ] Check difficulty selection
- [ ] Complete a quiz and verify the score
- [ ] Confirm results are saved
- [ ] Refresh the page and verify saved results
- [ ] Check leaderboard information
- [ ] Check student statistics
- [ ] Test the deployed website and backend

## 🎓 Project Information

- **Project Name:** AI Quiz Battle
- **Project Type:** Full-Stack Web Application
- **Domain:** Educational Technology
- **Purpose:** To support interactive CSE learning and performance tracking.

## 🔮 Future Enhancements

- Personalised quiz recommendations
- More CSE subjects and question sets
- Detailed performance charts
- Persistent production database with backups
- Automated testing and accessibility improvements

## 👩‍💻 Developer

**GitHub:** https://github.com/jahnaviathi7

---

*Built to make learning Computer Science more interactive, engaging, and competitive.*
