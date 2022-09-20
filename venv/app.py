
from flask import Flask ,render_template,request		


app = Flask(__name__)


@app.route("/",methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        if request.form.get("F_student") == 'student':
            return render_template('student.html')
        if request.form.get("F_teacher") == 'teacher':
            return render_template('teacher.html')
    return render_template("index.html");   

@app.route("/student",methods = ['GET','POST'])
def student():
    return render_template("student.html")

@app.route("/teacher",methods = ['GET','POST'])
def teacher():
    return render_template("teacher.html")
if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True) 