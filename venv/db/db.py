import sqlite3
import os

# Directory is fixed to db folder
os.chdir(os.path.dirname(__file__))
print(os.getcwd())

db = sqlite3.connect(os.getcwd()+'/test.db')
print("Database Connected Sucessfully!")

insertion_query = f"""INSERT INTO QUIZ(QUESTION, OPTION1, OPTION2, OPTION3, OPTION4, CORRECT_ANSWER, STATUS) 
VALUES(?, ?, ?, ?, ?, ?, ?)"""
key = 'y'
while key == 'y':
    question = input("Enter Your Question: ")
    option1 = input("Enter Option 1: ")
    option2 = input("Enter Option 2: ")
    option3 = input("Enter Option 3: ")
    option4 = input("Enter Option 4: ")
    correct = input("Enter Correct Answer: ")
    db.execute(insertion_query, (question, option1,
               option2, option3, option4, correct, "Inactive"))
    db.commit()
    print("Values Entered!")
    key = input("Do you want to add a new value(y/n)? ")
