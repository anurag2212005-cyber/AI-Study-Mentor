import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/learn")
def learn():
    return render_template("quiz.html")

@app.route("/quiz")
def quiz():
    return render_template("quiz_game.html")

@app.route("/planner", methods=["GET", "POST"])
def planner():
    plan = None
    if request.method == "POST":
        plan = {
            "subject": request.form.get("subject", ""),
            "topic": request.form.get("topic", ""),
            "hours": request.form.get("hours", "")
        }
    return render_template("planner.html", plan=plan)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
