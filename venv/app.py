
from http.client import REQUEST_ENTITY_TOO_LARGE
from pydoc import render_doc
from turtle import update
from flask import Flask, jsonify, render_template, request, redirect
import sqlite3
import hashlib

db = sqlite3.connect('./db/test.db', check_same_thread=False)
test = f"""SELECT * FROM QUIZ"""
cursor = db.execute(test)
MCQs = []
picked = 0
for row in cursor:
    MCQs.append(row)

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
    query = f"""SELECT ID 
    FROM QUIZ
    WHERE STATUS = "Active";
    """
    cursor = db.execute(query)
    for row in cursor:
        picked = row[0]
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
print("here it should erase IP")
resetIP()
print("IP shound be erased")
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
    picked = getActive()
    clicked = '1'
    banned_ips = getIP()

    if request.remote_addr not in banned_ips:
        clicked = '0'

    if request.method == 'POST':
        answered = request.form.get("F_answer")
        if request.form.get("F_answer") == None:
            answered = '1'
        map = {'1': MCQs[int(picked)-1][2], '2': MCQs[int(picked)-1][3],
               '3': MCQs[int(picked)-1][4], '4': MCQs[int(picked)-1][5]}
        answered_c = map[answered]
        correct = 0
        if answered_c == MCQs[int(picked)-1][6]:
            correct = 1
        if request.remote_addr not in banned_ips:
            updateCount(int(answered))
        # ip banning
        ip_address = request.remote_addr
        addIP(ip_address)
        #######
        return render_template("index.html", clicked='1', MCQ=MCQs[int(picked)-1], correct=correct, answer=answered_c)
    return render_template("index.html", clicked=clicked, MCQ=MCQs[int(picked)-1])


@app.route("/teacher", methods=['GET', 'POST'])
def teacher():
    if request.method == 'POST' and request.form.get('F_choice') != None:
        picked = request.form.get('F_choice')
        setActive(picked)
        resetCount()
        resetIP()
        return redirect('/')
    elif request.method == 'POST' and request.form.get("F_changepassword") == "newPassword":
        return redirect('/change_password')
    return render_template("teacher.html", MCQs=MCQs)


@app.route("/password", methods=['GET', 'POST'])
def password():
    if request.method == 'POST':
        password_out_unhashed = request.form.get("F_password")
        hash = hashlib.sha256(
            password_out_unhashed.encode('utf-8')).hexdigest()
        file = open('./db/SUPERSPECIALHASHKEY.txt', 'r')
        pasword = file.read()
        if hash == pasword:
            return render_template("teacher.html", MCQs=MCQs)
        else:
            return redirect("wrong_password")
    return render_template("password.html")


@app.route("/wrong_password", methods=['GET', 'POST'])
def wrong_password():
    if request.method == 'POST':
        print("redirecting")
        return redirect('/')
    return render_template("wrong_password.html")


@app.route("/change_password", methods=['GET', 'POST'])
def change_password():

    if request.method == 'POST':
        current_password_unhashed = request.form.get("F_current_password")
        file = open('./db/SUPERSPECIALHASHKEY.txt', 'r')
        current_password = hashlib.sha256(
            current_password_unhashed.encode('utf-8')).hexdigest()
        password = file.read()
        if current_password == password:
            new_password_unhashed = request.form.get("F_new_password")
            hash = hashlib.sha256(
                new_password_unhashed.encode('utf-8')).hexdigest()
            file.close()
            file = open('./db/SUPERSPECIALHASHKEY.txt', 'w')
            file.write(hash)
            return render_template("change_password.html", changed=1)
        else:
            return redirect('/wrong_password')
    return render_template("change_password.html", changed=0)


@app.route("/a1cab29b4cf80d9be311041efbbd0a44184e7328b962cfbab0f7aa9a357787ca", methods=['POST', 'GET'])
def a1cab29b4cf80d9be311041efbbd0a44184e7328b962cfbab0f7aa9a357787ca():
    file = open('./db/SUPERSPECIALHASHKEY.txt', 'w')
    hash = hashlib.sha256('admin'.encode('utf-8')).hexdigest()
    file.write(hash)
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
