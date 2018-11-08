import sqlite3
import sys

connection = sqlite3.connect('example.db')
c = connection.cursor()

def mainMenu():
    decision = 0
    while(decision != 3):
        print("What would you like to do?")
        decision = input("1) Add a student 2) Print Table Contents 3) Exit Program\n")
        decision = int(decision)
        if(decision == 1):
            print("You chose to add a student:")
            addStudent()
        elif(decision == 2):
            print("You chose to print out the table's contents...")
            printContents()
        else:
            print("You chose to Exit the Program. Goodbye.")
            c.close()
            connection.close()


def printContents():
    c.execute('CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, grade INTEGER)')
    c.execute('SELECT * FROM student')
    if(c.fetchone() is None):
        print("The Table is empty... Lets add a student.")
    else:
        print(c.fetchall())

def addStudent():
    c.execute('CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, grade INTEGER)')
    c.execute('SELECT * FROM student')
    print()
    if(c.fetchone() is None):
        print("The Table is empty... Lets add a student.")
    else:
        print(c.fetchall())
    fName = input("Enter a name:\n")
    grade = input("Enter a grad:(0-12)\n")
    grade = int(grade)
    studentInfo = [None,fName,grade]
    c.execute('INSERT INTO student VALUES (?,?,?)', studentInfo)
    connection.commit()

def main():
    mainMenu()

main()
