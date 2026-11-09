AI Study Mentor - ready-to-deploy Flask project

Files
- app.py: Flask application
- templates/index.html: home page
- templates/quiz.html: Learn & Explore
- templates/quiz_game.html: Smart Quiz Arena
- templates/planner.html: Study Planner
- requirements.txt: Python dependencies
- Procfile: hosting start command

Run locally (Windows)
1. Open this folder in VS Code.
2. Open Terminal > New Terminal.
3. Run: py -m pip install -r requirements.txt
4. Run: py app.py
5. Open http://127.0.0.1:5000

Deploy
This project is prepared for a Python web host that supports Gunicorn. Use build command: pip install -r requirements.txt
Use start command: gunicorn app:app

Note: This is a student learning-project starter. The learning lessons and quiz questions are sample content, not a complete official NCERT syllabus. Browser speech depends on the visitor's device/browser voice support.
