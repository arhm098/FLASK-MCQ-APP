import sqlite3
import os

# Directory is fixed to db folder
os.chdir(os.path.dirname(__file__))
print(os.getcwd())


db = sqlite3.connect(os.getcwd()+'/test.db')
print("Database Connected Sucessfully!")

creation_query_quiz = f"""CREATE TABLE QUIZ
(ID INTEGER PRIMARY KEY,
QUESTION TEXT NOT NULL,
OPTION1 TEXT NOT NULL,
OPTION2 TEXT NOT NULL,
OPTION3 TEXT NOT NULL,
OPTION4 TEXT NOT NULL,
CORRECT_ANSWER TEXT NOT NULL,
STATUS TEXT NOT NULL)"""

creation_query_count = f"""CREATE TABLE COUNT
(OPTION1 INTEGER NOT NULL,
OPTION2 INTEGER NOT NULL,
OPTION3 INTEGER NOT NULL,
OPTION4 INTEGER NOT NULL
)"""

creation_query_ip = f"""CREATE TABLE BANNED_IP
(IP TEXT NOT NULL)"""

count_initialize = f"""INSERT INTO COUNT(OPTION1, OPTION2, OPTION3, OPTION4)
VALUES(0,0,0,0)
    """

creation_password = f"""CREATE TABLE PASSWORD
(PASSWORD TEXT PRIMARY KEY)"""
password_intialize = f"""INSERT INTO PASSWORD(PASSWORD)
VALUES('8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918')"""
db.execute(creation_query_quiz)
db.execute(creation_query_count)
db.execute(creation_query_ip)
db.execute(creation_password)
db.execute(password_intialize)
print("Tables Created!")

db.execute(count_initialize)
db.commit()
print("Count data Initialized")
