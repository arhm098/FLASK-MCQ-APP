from http.client import REQUEST_ENTITY_TOO_LARGE
from pydoc import render_doc
from flask import Flask, render_template, request, redirect
import sqlite3

db = sqlite3.connect('../test.db')
test = f"""SELECT * FROM QUIZ"""
cursor = db.execute(test)
MCQs = []
picked = 0
for row in cursor:
    MCQs.append(row)

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    file = open('./db/secretspecial.txt', 'r')
    picked = file.read()
    print(picked)
    if request.method == 'POST':
        if request.form.get("F_student") == 'student':
            return render_template('student.html', clicked='0', MCQ=MCQs[int(picked)-1])
        if request.form.get("F_teacher") == 'teacher':
            return render_template('teacher.html', MCQs=MCQs)
    return render_template("index.html")


@app.route("/student", methods=['GET', 'POST'])
def student():
    file = open('./db/secretspecial.txt', 'r')
    picked = file.read()
    print(picked)
    if request.method == 'POST':
        answered = request.form.get("F_answer")
        map = {'1': MCQs[int(picked)-1][2], '2': MCQs[int(picked)-1][3],
               '3': MCQs[int(picked)-1][4], '4': MCQs[int(picked)-1][5]}
        answered_c = map[answered]
        correct = 0
        if answered_c == MCQs[int(picked)-1][6]:
            correct = 1
        return render_template("student.html", clicked='1', MCQ=MCQs[int(picked)-1], correct=correct, answer=answered_c)
    return render_template("student.html",clicked='0',MCQ=MCQs[int(picked)-1])


@app.route("/teacher", methods=['GET', 'POST'])
def teacher():
    if request.method == 'POST':
        picked = request.form.get('F_choice')
        file = open('./db/secretspecial.txt', 'w')
        file.write(picked)
        return redirect('/')
    return render_template("teacher.html", MCQs=MCQs)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
