import sqlite3

db = sqlite3.connect('./test.db')
print("Database Connected Sucessfully!")

# creation_query = f"""CREATE TABLE QUIZ
# (ID INTEGER PRIMARY KEY,
# QUESTION TEXT NOT NULL,
# OPTION1 TEXT NOT NULL,
# OPTION2 TEXT NOT NULL,
# OPTION3 TEXT NOT NULL,
# OPTION4 TEXT NOT NULL,
# CORRECT_ANSWER TEXT NOT NULL)"""

# db.execute(creation_query)
# print("Tables Created!")


insertion_query = f"""INSERT INTO QUIZ(QUESTION, OPTION1, OPTION2, OPTION3, OPTION4, CORRECT_ANSWER) 
VALUES(?, ?, ?, ?, ?, ?)"""
key = 'y'
while key != 'n':
    question = input("Enter Your Question: ")
    option1 = input("Enter Option 1: ")
    option2 = input("Enter Option 2: ")
    option3 = input("Enter Option 3: ")
    option4 = input("Enter Option 4: ")
    correct = input("Enter Correct Answer: ")
    db.execute(insertion_query, (question, option1,
               option2, option3, option4, correct))
    db.commit()
    print("Values Entered!")
    key = input("Do you want to add a new value(y/n)? ")

test = f"""SELECT * FROM QUIZ"""
cursor = db.execute(test)

for row in cursor:
    print(row[0])
    print(row[1])
    print(row[2])
    print(row[3])
    print(row[4])
    print(row[5])
    print(row[6])
