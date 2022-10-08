import sqlite3
import os

os.chdir('./')


db = sqlite3.connect(os.getcwd()+'/test.db')
print("Database Connected Sucessfully!")

test = f"""SELECT * FROM QUIZ"""
cursor = db.execute(test)
MCQs = []
picked = 0
for row in cursor:
    print(row)
