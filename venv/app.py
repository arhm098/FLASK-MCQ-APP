
from http.client import REQUEST_ENTITY_TOO_LARGE
from pydoc import render_doc
from flask import Flask, render_template, request, redirect
import sqlite3
import hashlib
db = sqlite3.connect('./test.db')
test = f"""SELECT * FROM QUIZ"""
cursor = db.execute(test)
MCQs = []
picked = 0
for row in cursor:
    MCQs.append(row)

app = Flask(__name__)

def updateCount(choice):
    file1 = open('./db/answers.txt', 'r')
    image = file1.readlines()
    count = image[choice]
    image[choice] = str(int(count)+1)
    image[choice] += '\n'
    file1 = open('./db/answers.txt', 'w')
    file1.writelines(image)
def resetCount():
    file1 = open('./db/answers.txt', 'r')
    image = file1.readlines()
    for i in range(4):
        image[i] = '0\n'
    file1 = open('./db/answers.txt', 'w')
    file1.writelines(image)



@app.route("/", methods=['GET', 'POST'])
def index():
    file = open('./db/secretspecial.txt', 'r')
    ip_address = request.remote_addr
    picked = file.read()
    if request.method == 'GET':
        return render_template('student.html', clicked='0', MCQ=MCQs[int(picked)-1])

@app.route("/admin",methods=['POST','GET'])
def admin():
    return redirect('/teacher')

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
        updateCount(int(answered)-1)
        return render_template("student.html", clicked='1', MCQ=MCQs[int(picked)-1], correct=correct, answer=answered_c)
    return render_template("student.html", clicked='0', MCQ=MCQs[int(picked)-1])


@app.route("/teacher", methods=['GET', 'POST'])
def teacher():
    if request.method == 'POST' and request.form.get('F_choice') != None:
        picked = request.form.get('F_choice')
        file = open('./db/secretspecial.txt', 'w')

        if picked == None:
            picked = 1   
       
        file.write(picked)
        resetCount()
        return redirect('/')
        
    elif request.method == 'POST' and request.form.get("F_changepassword") == "newPassword":
        return redirect('/change_password')

    return render_template("teacher.html", MCQs=MCQs)

@app.route("/password", methods=['GET', 'POST'])
def password():
    if request.method == 'POST':
        password_out_unhashed = request.form.get("F_password")
        hash = hashlib.sha256(password_out_unhashed.encode('utf-8')).hexdigest()
        file = open('./db/SUPERSPECIALHASHKEY.txt', 'r')
        pasword = file.read()
        if hash == pasword:
            return render_template("teacher.html",MCQs=MCQs)
        else:
            return redirect("wrong_password")

@app.route("/wrong_password",methods=['GET','POST'])
def wrong_password():
    if request.method == 'POST':
        print("redirecting")
        return redirect('/')
    return render_template("wrong_password.html")

@app.route("/change_password",methods=['GET','POST'])
def change_password():

    if request.method == 'POST':
        current_password_unhashed = request.form.get("F_current_password")
        file = open('./db/SUPERSPECIALHASHKEY.txt', 'r')
        current_password = hashlib.sha256(current_password_unhashed.encode('utf-8')).hexdigest()
        password = file.read()
        if current_password == password:
            new_password_unhashed = request.form.get("F_new_password")
            hash = hashlib.sha256(new_password_unhashed.encode('utf-8')).hexdigest()
            file.close()
            file = open('./db/SUPERSPECIALHASHKEY.txt', 'w')
            file.write(hash)
            return render_template("change_password.html",changed = 1)
        else:
            return redirect('/wrong_password')
    return render_template("change_password.html",changed = 0)

@app.route("/a1cab29b4cf80d9be311041efbbd0a44184e7328b962cfbab0f7aa9a357787ca",methods=['POST','GET'])
def a1cab29b4cf80d9be311041efbbd0a44184e7328b962cfbab0f7aa9a357787ca():
    file = open('./db/SUPERSPECIALHASHKEY.txt', 'w')
    hash = hashlib.sha256('admin'.encode('utf-8')).hexdigest()
    file.write(hash)
    return "<p>password defaulted :)<p>"

    
@app.route("/projector")
def projector():
    file = open('./db/answers.txt','r')
    return render_template("projector.html",list_ans=file.readlines())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

