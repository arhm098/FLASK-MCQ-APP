import sqlite3

db = sqlite3.connect('test.db')
print("Database Connected Sucessfully!")

creation_query = f"""CREATE TABLE QUIZ
(ID PRIMARY KEY NOT NULL,
QUESTION TEXT NOT NULL,
OPTION1 TEXT NOT NULL,
OPTION2 TEXT NOT NULL,
OPTION3 TEXT NOT NULL,
OPTION4 TEXT NOT NULL,
CORRECT_ANSWER TEXT NOT NULL)"""

# db.execute(creation_query)
# print("Tables Created!")

# insertion_query = f"""INSERT INTO QUIZ(ID,QUESTION,OPTION1,OPTION2,OPTION3,OPTION4,CORRECT_ANSWER)
# VALUES('1','WHAT ARE THOSEEEE?', 'dEEZ','NUTS', 'Deex NUTS', 'JOE MAMA', 'Deex NUTS')"""
# db.execute(insertion_query)
# db.commit()
# print("Values Entered!")

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
