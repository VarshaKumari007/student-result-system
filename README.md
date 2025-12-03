# 🎓 Student Result Management System  
A simple and functional **Python + MySQL** project that manages student records, calculates results, and performs CRUD operations.  
This project runs fully in the **terminal (CLI)** and is ideal for beginners and freshers showcasing backend and database skills.

---

## 🚀 Features
- Add new student with subject-wise marks  
- Update marks of an existing student  
- Delete a student record  
- Search student by roll number  
- View all students in tabular format  
- Auto-calculate total, percentage, and pass/fail status  
- Uses MySQL database for secure data storage  
- Clean, modular Python code with comments  

---

## 🛠️ Tech Stack
- **Python 3**
- **MySQL Database**
- **MySQL Connector for Python**
- **Tabulate Library** (for clean table output)

---

## 📂 Project Structure
student-result-system/
│
├── main.py # Main application code
├── schema.sql # Database + table creation file
├── README.md # Project description
├── .gitignore
└── LICENSE

---

## 🧩 Database Setup

1. Open MySQL Workbench / terminal  
2. Run the SQL file:

```sql
SOURCE schema.sql;
