
from http.client import REQUEST_ENTITY_TOO_LARGE
from pydoc import render_doc
from flask import Flask, render_template, request
import sqlite3

db = sqlite3.connect('../test.db')
test = f"""SELECT * FROM QUIZ"""
cursor = db.execute(test)

for row in cursor:

    question = row[1]
    option1 = row[2]
    option2 = row[3]
    option3 = row[4]
    option4 = row[5]
    answer = row[6]

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get("F_student") == 'student':
            return render_template('student.html', MCQ_HEADING=question, option_1=option1, option_2=option2, option_3=option3, option_4=option4, right_option=answer)
        if request.form.get("F_teacher") == 'teacher':
            return render_template('teacher.html')
    return render_template("index.html")


@app.route("/student", methods=['GET', 'POST'])
def student():
    if request.method == 'POST':
        answered = request.form.get("F_answer")
        return render_template("answer.html", Answer=answered, right_answer=answer)
    return render_template("student.html")


@app.route("/teacher", methods=['GET', 'POST'])
def teacher():
    return render_template("teacher.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
