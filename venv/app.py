
from http.client import REQUEST_ENTITY_TOO_LARGE
from pydoc import render_doc
from turtle import update
from flask import Flask, jsonify, render_template, request, redirect
import sqlite3
import hashlib
db = sqlite3.connect('./db/test.db', check_same_thread=False)

def getHash():
    passW = []
    query = f"""SELECT * FROM PASSWORD"""
    cursor = db.execute(query)
    for row in cursor:
        passW.append(row)
    print(passW)
    return passW
    
def changeHash(HASH):
    query = f"""UPDATE PASSWORD
    SET PASSWORD = "{HASH}";
    """
    db.execute(query)
    db.commit()

def eraseMCQ():
    test = f"""DROP TABLE QUIZ"""
    db.execute(test)
    db.commit()
    creation_query_quiz = f"""CREATE TABLE QUIZ
        (ID INTEGER PRIMARY KEY,
        QUESTION TEXT NOT NULL,
        OPTION1 TEXT NOT NULL,
        OPTION2 TEXT NOT NULL,
        OPTION3 TEXT NOT NULL,
        OPTION4 TEXT NOT NULL,
        CORRECT_ANSWER TEXT NOT NULL,
        STATUS TEXT NOT NULL)"""
    db.execute(creation_query_quiz)
    db.commit()

def fetchMCQ():
    MCQs = []
    test = f"""SELECT * FROM QUIZ"""
    cursor = db.execute(test)
    for row in cursor:
        MCQs.append(row)
    return MCQs

def addMCQ(question, option1,option2, option3, option4, correct):
    insertion_query = f"""INSERT INTO QUIZ(QUESTION, OPTION1, OPTION2, OPTION3, OPTION4, CORRECT_ANSWER, STATUS) 
    VALUES(?, ?, ?, ?, ?, ?, ?)"""
    db.execute(insertion_query, (question, option1,
    option2, option3, option4, correct, "Inactive"))
    db.commit()

def setActive(picked):
    query = f"""UPDATE QUIZ
    SET STATUS = "Inactive";
    """
    db.execute(query)
    db.commit()
    query2 = f"""UPDATE QUIZ
    SET STATUS = "Active"
    WHERE ID = {picked};
    """
    db.execute(query2)
    db.commit()


def getActive():
    picked = []
    test = f"""SELECT * FROM QUIZ
    WHERE STATUS = "Active" """
    cursor = db.execute(test)
    for row in cursor:
        picked.append(row)
    return picked

def getCount():
    query = f"""SELECT * FROM COUNT;"""
    cursor = db.execute(query)
    for row in cursor:
        count = row
    return count


def updateCount(choice):
    query = f"""UPDATE COUNT
    SET OPTION{choice} = OPTION{choice} + 1;
    """
    db.execute(query)
    db.commit()


def resetCount():
    query = f"""UPDATE COUNT
    SET OPTION1 = 0,
     OPTION2 = 0,
     OPTION3 = 0,
     OPTION4 = 0
    ;"""
    db.execute(query)
    db.commit()


def addIP(ip):
    query = f"""INSERT INTO BANNED_IP(IP)
    VALUES(?);"""
    db.execute(query, (ip,))
    db.commit()


def resetIP():
    query = f"""DELETE FROM BANNED_IP;"""
    db.execute(query)
    db.commit()


def getIP():
    query = f"""SELECT * FROM BANNED_IP;"""
    cursor = db.execute(query)
    ips = []
    for row in cursor:
        ips.append(row[0])
    return ips

resetIP()

app = Flask(__name__)

# Helper Functions




@app.route("/update_count", methods=['GET'])
def update_count():
    if request.method == "GET":
        new_counts = getCount()
        return render_template("update_count.html", list_ans=new_counts)
    # return jsonify(new_counts)


@app.route("/", methods=['GET', 'POST'])
def index():
    correct = 0
    picked = getActive()
    picked = picked[0]
    map = {'1': picked[2], '2': picked[3],'3': picked[4], '4': picked[5]}
    clicked = '1'
    banned_ips = getIP()
    if request.remote_addr not in banned_ips:
        clicked = '0'
    if request.method == 'POST':
        answered = request.form.get("F_answer")
        if request.form.get("F_answer") == None:
            answered = '1'
        print(map)
        answered_c = map[answered]
        if answered_c == picked[6]:
            correct = 1
        if request.remote_addr not in banned_ips:
            updateCount(int(answered))
        # ip banning
        ip_address = request.remote_addr
        addIP(ip_address)
        #######
        return render_template("index.html", clicked='1', MCQ=picked, correct=correct, answer=answered_c)
    return render_template("index.html", clicked=clicked, MCQ=picked)


@app.route("/teacher", methods=['GET', 'POST'])
def teacher():
    if request.method == 'POST' and request.form.get('F_choice') != None:
        choice = request.form.get('F_choice')
        setActive(choice)
        resetCount()
        resetIP()
        return redirect('/')
    elif request.method == 'POST' and request.form.get("F_changepassword") == "newpassword":
        return redirect('/change_password')
    elif request.method == 'POST' and request.form.get("F_Question") != None and request.form.get("F_choice1") != None:
        question = request.form.get("F_Question")
        choice1 = request.form.get("F_choice1")
        choice2 = request.form.get("F_choice2")
        choice3 = request.form.get("F_choice3")
        choice4 = request.form.get("F_choice4")
        answer = request.form.get("F_answer")
        addMCQ(question, choice1,choice2, choice3, choice4, answer)
    elif request.method == 'POST' and request.form.get("F_eraseMCQs") == "remove all mcqs":
        eraseMCQ()
    return render_template("teacher.html", MCQs=fetchMCQ(), auth = '0')


@app.route("/password", methods=['GET', 'POST'])
def password():
    if request.method == 'POST':
        password_out_unhashed = request.form.get("F_password")
        hash = hashlib.sha256(
            password_out_unhashed.encode('utf-8')).hexdigest()
        password = getHash()
        password = password[0][0]
        if hash == password:
            return render_template("teacher.html", MCQs=fetchMCQ(), auth = '1')
        else:
            return redirect("wrong_password")
    return render_template("password.html")


@app.route("/wrong_password", methods=['GET', 'POST'])
def wrong_password():
    if request.method == 'POST':
        return redirect('/')
    return render_template("wrong_password.html")


@app.route("/change_password", methods=['GET', 'POST'])
def change_password():

    if request.method == 'POST':
        current_password_unhashed = request.form.get("F_current_password")
        current_password = hashlib.sha256(
            current_password_unhashed.encode('utf-8')).hexdigest()
        password = getHash()
        password = password[0][0]
        if current_password == password:
            new_password_unhashed = request.form.get("F_new_password")
            hash = hashlib.sha256(
                new_password_unhashed.encode('utf-8')).hexdigest()
            changeHash(hash)
            return render_template("change_password.html", changed=1)
        else:
            return redirect('/wrong_password')
    return render_template("change_password.html", changed=0)


@app.route("/a1cab29b4cf80d9be311041efbbd0a44184e7328b962cfbab0f7aa9a357787ca", methods=['POST', 'GET'])
def a1cab29b4cf80d9be311041efbbd0a44184e7328b962cfbab0f7aa9a357787ca():
    hash = hashlib.sha256('admin'.encode('utf-8')).hexdigest()
    changeHash(hash)
    return "<p>password defaulted :)<p>"


@app.route("/projector")
def projector():
    count = getCount()
    return render_template("projector.html", list_ans=count)


@app.route("/admin", methods=['POST', 'GET'])
def admin():
    return redirect('/password')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
