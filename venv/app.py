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

    question = row[1]
    option1 = row[2]
    option2 = row[3]
    option3 = row[4]
    option4 = row[5]
    answer = row[6]
    MCQs.append(row)

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    print(picked)
    if request.method == 'POST':
        if request.form.get("F_student") == 'student':
            print(picked)
            print(MCQs[picked])
            return render_template('student.html', clicked='0', MCQs=MCQs)
        if request.form.get("F_teacher") == 'teacher':
            return render_template('teacher.html', MCQs=MCQs)
    return render_template("index.html")


@app.route("/student", methods=['GET', 'POST'])
def student():
    picked = open('./db/secretspecial.txt', 'r')
    if request.method == 'POST':
        answered = request.form.get("F_answer")
        map = {'1': MCQs[picked][2], '2': MCQs[picked][3],
               '3': MCQs[picked][4], '4': MCQs[picked][5]}
        answered_c = map[answered]
        correct = 0
        if answered_c == answer:
            correct = 1
        return render_template("student.html", clicked='1', MCQs=MCQs, correct=correct, answer=answered_c)
    return render_template("student.html")


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
