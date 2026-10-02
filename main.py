from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    name = request.form["name"]
    maths = float(request.form["maths"])
    python = float(request.form["python"])
    communication = float(request.form["communication"])
    internship = request.form["internship"]
    projects = int(request.form["projects"])

    total = maths + python + communication

    if total >= 240:
        status = "Excellent"
    elif total >= 190:
        status = "Average"
    else:
        status = "Needs Improvement"

    return render_template(
        "result.html",
        name=name,
        total=total,
        status=status,
        internship=internship,
        projects=projects
    )


@app.route("/dashboard")
def dashboard():
    data = pd.read_csv("students.csv")

    total_students = len(data)
    avg_python = round(data["Python"].mean(), 2)
    avg_communication = round(data["Communication"].mean(), 2)
    internship_students = len(
        data[data["Internship"] == "Yes"]
    )

    # Python Score Chart
    plt.figure(figsize=(8, 5))
    plt.bar(data["Name"], data["Python"])
    plt.xlabel("Students")
    plt.ylabel("Python Score")
    plt.title("Python Scores")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("static/python_chart.png")
    plt.close()

    # Internship Analysis Chart
    internship_counts = data["Internship"].value_counts()

    plt.figure(figsize=(6, 5))
    plt.bar(
        internship_counts.index,
        internship_counts.values
    )
    plt.xlabel("Internship")
    plt.ylabel("Number of Students")
    plt.title("Internship Analysis")
    plt.tight_layout()
    plt.savefig("static/internship_chart.png")
    plt.close()

    return render_template(
        "dashboard.html",
        total_students=total_students,
        avg_python=avg_python,
        avg_communication=avg_communication,
        internship_students=internship_students
    )


if __name__ == "__main__":
    app.run(debug=True)