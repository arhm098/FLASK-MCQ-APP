import sqlite3
import os

# Directory is fixed to db folder
os.chdir(os.path.dirname(__file__))
print(os.getcwd())


db = sqlite3.connect(os.getcwd()+'/test.db')
print("Database Connected Sucessfully!")

# test = f"""SELECT * FROM QUIZ"""
# cursor = db.execute(test)
# MCQs = []
# picked = 0
# for row in cursor:
#     print(row)


test2 = f"""SELECT * FROM COUNT"""
cursor = db.execute(test2)
for row in cursor:
    print(row)
