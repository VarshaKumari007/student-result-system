"""
Student Result Management System
Technology: Python + MySQL
Author: Varsha Kumari

Features:
- Add student details with marks
- Update marks
- Delete student
- Search by roll number
- View all students
- Calculate total, percentage & status (Pass/Fail)
"""

import mysql.connector
from tabulate import tabulate

# ---------------------------
#   MySQL Database Connection
# ---------------------------
def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",      # <-- Put your MySQL password here
            database="studentdb"
        )
        return connection
    except mysql.connector.Error as err:
        print("Error:", err)
        return None


# ---------------------------
#   Add new student
# ---------------------------
def add_student():
    con = connect_db()
    cur = con.cursor()

    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    st_class = input("Enter Class: ")

    maths = int(input("Maths Marks: "))
    physics = int(input("Physics Marks: "))
    chemistry = int(input("Chemistry Marks: "))

    query = """
        INSERT INTO students (roll_no, name, class, maths, physics, chemistry)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    cur.execute(query, (roll, name, st_class, maths, physics, chemistry))
    con.commit()

    print("\n✔ Student added successfully!\n")


# ---------------------------
#   Update Marks
# ---------------------------
def update_marks():
    con = connect_db()
    cur = con.cursor()

    roll = input("Enter Roll Number to Update: ")

    print("\nEnter new marks:")
    maths = int(input("Maths: "))
    physics = int(input("Physics: "))
    chemistry = int(input("Chemistry: "))

    query = """
        UPDATE students 
        SET maths = %s, physics = %s, chemistry = %s
        WHERE roll_no = %s
    """

    cur.execute(query, (maths, physics, chemistry, roll))
    con.commit()

    print("\n✔ Marks updated successfully!\n")


# ---------------------------
#   Delete Student
# ---------------------------
def delete_student():
    con = connect_db()
    cur = con.cursor()

    roll = input("Enter Roll Number to Delete: ")

    query = "DELETE FROM students WHERE roll_no = %s"
    cur.execute(query, (roll,))
    con.commit()

    print("\n✔ Student deleted successfully!\n")


# ---------------------------
#   Search Student
# ---------------------------
def search_student():
    con = connect_db()
    cur = con.cursor()

    roll = input("Enter Roll Number to Search: ")

    query = "SELECT * FROM students WHERE roll_no = %s"
    cur.execute(query, (roll,))
    data = cur.fetchone()

    if data:
        headers = ["ID", "Roll No", "Name", "Class", "Maths", "Physics", "Chemistry", "Created At"]
        print("\n", tabulate([data], headers=headers, tablefmt="fancy_grid"))
    else:
        print("\n❌ No student found with that roll number.\n")


# ---------------------------
#   View All Students
# ---------------------------
def view_all():
    con = connect_db()
    cur = con.cursor()

    query = "SELECT * FROM students"
    cur.execute(query)
    data = cur.fetchall()

    if data:
        headers = ["ID", "Roll No", "Name", "Class", "Maths", "Physics", "Chemistry", "Created At"]
        print("\n", tabulate(data, headers=headers, tablefmt="fancy_grid"))
    else:
        print("\n❌ No records found.\n")


# ---------------------------
#   Calculate Result
# ---------------------------
def calculate_result():
    con = connect_db()
    cur = con.cursor()

    roll = input("Enter Roll Number: ")

    query = "SELECT maths, physics, chemistry FROM students WHERE roll_no = %s"
    cur.execute(query, (roll,))
    data = cur.fetchone()

    if data:
        maths, physics, chemistry = data
        total = maths + physics + chemistry
        percent = total / 3

        status = "Pass" if maths >= 33 and physics >= 33 and chemistry >= 33 else "Fail"

        print("\n------------- RESULT ---------------")
        print(f"Maths: {maths}")
        print(f"Physics: {physics}")
        print(f"Chemistry: {chemistry}")
        print(f"Total: {total}")
        print(f"Percentage: {percent:.2f}%")
        print(f"Status: {status}")
        print("------------------------------------\n")

    else:
        print("\n❌ Student not found.\n")


# ---------------------------
#   Main Menu
# ---------------------------
def menu():
    while True:
        print("""
==============================
  Student Result System
==============================
1. Add Student
2. Update Marks
3. Delete Student
4. Search Student
5. View All Students
6. Calculate Result
7. Exit
""")

        choice = input("Enter choice (1-7): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            update_marks()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            search_student()
        elif choice == "5":
            view_all()
        elif choice == "6":
            calculate_result()
        elif choice == "7":
            print("\n✔ Thank you for using the system!")
            break
        else:
            print("\n❌ Invalid choice. Try again.\n")


# Start the program
menu()
