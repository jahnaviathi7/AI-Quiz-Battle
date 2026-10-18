🎯 AI Quiz Battle
Test your CSE knowledge. Compete. Improve.
AI Quiz Battle is a full-stack web application that helps students
practise Computer Science Engineering (CSE) topics through interactive
quizzes. Students can register, log in, choose quiz categories and
difficulty levels, complete timed quizzes, review scores, track
progress, and compare results on a leaderboard.
🔗 Project Links
- Live Website: https://ai-quiz-battle-llmz.onrender.com/
- GitHub Repository:
  https://github.com/jahnaviathi7/AI-Quiz-Battle
- Backend API: https://ai-quiz-battle-backend.onrender.com
- API Documentation:
  https://ai-quiz-battle-backend.onrender.com/docs
- Backend Health Check:
  https://ai-quiz-battle-backend.onrender.com/api/health
✨ Features
- Student registration and login
- Category-based CSE quizzes
- Difficulty selection
- Quiz timer
- Automatic score calculation
- XP and streak tracking
- Saved quiz results
- Student performance statistics
- Leaderboard
- Backend REST API
- Deployed frontend and backend
🧰 Technologies Used
  Technology              Role
  React                   Builds the interactive user interface
  Vite                    Frontend development server and production build
  JavaScript, HTML, CSS   Frontend logic, structure, and styling
  Python                  Backend application logic
  FastAPI                 REST API and request handling
  Pydantic                Request-data validation
  SQLite                  Stores student and quiz-result data
  Git and GitHub          Version control and source-code hosting
  Render                  Hosts the web application and backend API
The quiz-generation component is implemented in the backend. Describe
its exact AI provider or question-generation method according to the
code in backend/ai_engine.py.
🏗️ How It Works
1. A student opens the website and registers or logs in.
2. The student selects a quiz category and difficulty.
3. The React frontend sends requests to the FastAPI backend.
4. The backend generates or retrieves quiz questions using the
   question-generation component.
5. The student answers the questions before the timer ends.
6. The application calculates the score and submits the result.
7. Student statistics and leaderboard information are retrieved from
   the backend and displayed on the website.
Student
   |
   v
React + Vite Frontend
   |
   | HTTP requests / JSON responses
   v
FastAPI Backend
   |--------------------|
   v                    v
Quiz Engine         SQLite Database
   |                    |
   |--------------------|
            |
            v
 Scores, Statistics and Leaderboard
            |
            v
       Frontend UI
📁 Project Structure
The project is organised into frontend and backend sections. Your exact
files may vary.
AI-Quiz-Battle/
├── README.md
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
└── backend/
    ├── main.py
    ├── database.py
    ├── ai_engine.py
    └── requirements.txt
🚀 Run the Project Locally
Prerequisites
- Node.js and npm
- Python 3
- Git (optional)
1. Download the source code
git clone https://github.com/jahnaviathi7/AI-Quiz-Battle.git
cd AI-Quiz-Battle
2. Start the backend
Open a terminal:
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
The local API should be available at http://127.0.0.1:8000.
Interactive API documentation is available at
http://127.0.0.1:8000/docs.
3. Start the frontend
Open a second terminal from the project root:
cd frontend
npm install
npm run dev
Open the local URL printed by Vite in the terminal.
Note: If your frontend uses a configured backend URL, ensure it
points to your local API when running locally. Keep production settings
and secrets out of public source code.
🧪 Testing Checklist
- [ ] Register a new account.
- [ ] Log in with valid credentials.
- [ ] Check that invalid login details are rejected.
- [ ] Generate quizzes for different categories.
- [ ] Verify that difficulty selection works.
- [ ] Complete a quiz and check the score.
- [ ] Confirm that the result is saved.
- [ ] Refresh the page and check saved results.
- [ ] Verify leaderboard data.
- [ ] Verify student statistics.
- [ ] Check the backend health endpoint.
- [ ] Test the deployed website in a browser.
🔐 Security and Data Notes
- Passwords should be stored as password hashes, not as plain text.
- Do not commit API keys, credentials, or private environment
  variables to GitHub.
- SQLite data on a hosting service may not persist across
  redeployments unless persistent storage is configured. Confirm the
  deployment's storage configuration before relying on it for
  long-term records.
- Use appropriate authentication and authorization checks before
  exposing private student data.
🎓 Academic and Portfolio Use
Project type: Full-stack web application
Domain: Educational technology / quiz-based learning
Purpose: Help students practise CSE topics and monitor quiz
performance.
When presenting this project in a review or interview, explain the
architecture, API endpoints, database design, question-generation
method, score calculation, testing process, and deployment setup. Be
ready to demonstrate the working features live.
🔮 Future Enhancements
- Personalised quizzes based on past performance
- More CSE subjects and question sets
- Detailed progress charts
- Additional accessibility and mobile usability improvements
- Persistent production database and automated backups
- More comprehensive automated tests
👩‍💻 Developer
GitHub: https://github.com/jahnaviathi7
If you find this project useful, visit the repository and explore the
source code.
