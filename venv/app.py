
from http.client import REQUEST_ENTITY_TOO_LARGE
from pydoc import render_doc
from flask import Flask ,render_template,request		


app = Flask(__name__)


@app.route("/",methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        if request.form.get("F_student") == 'student':
            return render_template('student.html',MCQ_HEADING = "This is the question that is being asked!",option_1="option 1",option_2="option 2",option_3="option 3",option_4="option 4",right_option='RIGHT ANSWER')
        if request.form.get("F_teacher") == 'teacher':
            return render_template('teacher.html')
    return render_template("index.html");   

@app.route("/student",methods = ['GET','POST'])
def student():
    if request.method == 'POST':
        answered = request.form.get("F_answer")
        return render_template("answer.html",answer = answered,right_answer="right answer")
    return render_template("student.html")

@app.route("/teacher",methods = ['GET','POST'])
def teacher():
    return render_template("teacher.html")

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True) 