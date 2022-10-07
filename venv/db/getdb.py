import sqlite3
import os

os.chdir('../')

    


db = sqlite3.connect('./test.db')
test = f"""SELECT * FROM QUIZ"""
cursor = db.execute(test)
MCQs = []
picked = 0
for row in cursor:
    print(row)
