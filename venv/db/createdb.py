import sqlite3
import os

os.chdir('./')


db = sqlite3.connect(os.getcwd()+'/test.db')
print("Database Connected Sucessfully!")

creation_query = f"""CREATE TABLE QUIZ
(ID INTEGER PRIMARY KEY,
QUESTION TEXT NOT NULL,
OPTION1 TEXT NOT NULL,
OPTION2 TEXT NOT NULL,
OPTION3 TEXT NOT NULL,
OPTION4 TEXT NOT NULL,
CORRECT_ANSWER TEXT NOT NULL)"""

db.execute(creation_query)
print("Tables Created!")