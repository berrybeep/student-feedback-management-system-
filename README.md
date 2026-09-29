# Student Feedback Management System

## 📌 Project Description

The **Student Feedback Management System** is a Python-based, menu-driven project designed to manage student information, subjects, advisors, student feedback, advisor feedback, ratings, and feedback statistics.

The system uses **CSV files** to store and manage data permanently. It provides a simple and user-friendly interface through which users can register students, add subjects and advisors, submit feedback, search records, calculate average ratings, and view feedback statistics.

---

## 🎯 Objectives

The main objectives of this project are:

- Register and manage student information
- Add and manage subjects
- Add and manage advisor information
- Collect student feedback
- Collect advisor feedback
- Search student, subject, advisor, and feedback records
- View student feedback history
- View subject-wise feedback
- Calculate average ratings
- Display feedback statistics
- Store data permanently using CSV files
- Provide basic input validation

---

## ✨ Features

### 1. Student Management

The Student Management section provides the following features:

- Register Student
- View All Students
- Search Student

### 2. Subject Management

The Subject Management section provides:

- Add Subject
- View All Subjects
- Search Subject

### 3. Advisor Management

The Advisor Management section provides:

- Add Advisor
- View All Advisors
- Search Advisor

### 4. Student Feedback Management

Students can provide feedback about their subjects and faculty.

Features include:

- Submit Student Feedback
- View All Feedback
- Search Feedback
- View Subject-wise Feedback
- View Student Feedback History
- Calculate Average Rating
- View Feedback Statistics

### 5. Advisor Feedback

The system also allows students to provide feedback about their advisors.

Students can rate:

- Academic Guidance
- Advisor Availability
- Communication
- Student Support
- Add Comments

---

## 📊 Feedback Rating System

The student feedback system uses a rating scale from **1 to 5**.

### Student Feedback Ratings

The following areas are rated:

- Teacher Quality
- Content Quality
- Doubt Clarification
- Faculty Interaction

### Advisor Feedback Ratings

The following areas are rated:

- Academic Guidance
- Advisor Availability
- Communication
- Student Support

A higher rating represents a more positive feedback score.

---

## 🛠️ Technologies Used

The project is developed using:

- **Python**
- **CSV Module**
- **OS Module**
- **Visual Studio Code**

### Python Modules

#### CSV Module

The `csv` module is used to:

- Create CSV files
- Store records
- Read records
- Search records
- Manage feedback data

#### OS Module

The `os` module is used to:

- Check whether files exist
- Manage file-related operations

---

## 📂 Project Structure

```text
Student-Feedback-Management-System/

│
├── main.py
├── README.md
│
├── students.csv
├── subjects.csv
├── advisors.csv
├── feedback.csv
└── advisor_feedback.csv
```

> The CSV files are created automatically when data is added through the program.

---

## 📋 Main Menu

The program provides the following menu options:

```text
1. Register Student
2. View All Students
3. Search Student
4. Add Subject
5. View All Subjects
6. Search Subject
7. Add Advisor
8. View All Advisors
9. Search Advisor
10. Submit Student Feedback
11. View All Feedback
12. Search Feedback
13. Subject-wise Feedback
14. Student Feedback History
15. Calculate Average Rating
16. Feedback Statistics
17. Submit Advisor Feedback
18. Exit
```

---

## 💾 Data Storage

The project uses CSV files to store information permanently.

### students.csv

Stores student registration details.

### subjects.csv

Stores subject and faculty information.

### advisors.csv

Stores advisor information.

### feedback.csv

Stores student feedback and ratings for different subjects.

The feedback includes:

- Teacher Quality
- Content Quality
- Doubt Clarification
- Faculty Interaction
- Suggestions

### advisor_feedback.csv

Stores feedback given by students about their advisors.

The feedback includes:

- Academic Guidance
- Advisor Availability
- Communication
- Student Support
- Comments

---

## 🔍 Search and Analysis

The system allows users to:

- Search students
- Search subjects
- Search advisors
- Search feedback
- View subject-wise feedback
- View student feedback history
- Calculate average ratings
- View feedback statistics

---

## 📈 Feedback Analysis

The system calculates average ratings from the feedback stored in the CSV files.

The feedback statistics feature provides an overview of the ratings submitted by students.

This helps organize and analyze student feedback related to:

- Teaching quality
- Course content
- Doubt clarification
- Faculty interaction
- Advisor support

---

## ✅ Input Validation

The system includes basic input validation for:

- Empty names
- Empty input fields
- Ratings between 1 and 5
- Required student and feedback information

This helps reduce incorrect or incomplete data entry.

---

## 🔄 Program Flow

The basic working process of the system is:

```text
Start
  ↓
Display Main Menu
  ↓
Select an Option
  ↓
Perform Selected Operation
  ↓
Read/Write Data Using CSV Files
  ↓
Display Result
  ↓
Return to Main Menu
  ↓
Exit
```

---

## ▶️ How to Run the Project

### Step 1: Install Python

Make sure Python is installed on your computer.

You can check whether Python is installed by running:

```text
python --version
```

### Step 2: Open the Project

Open the **Student-Feedback-Management-System** folder in **Visual Studio Code**.

### Step 3: Open the Python File

Open:

```text
main.py
```

### Step 4: Open the Terminal

In Visual Studio Code, open:

```text
Terminal → New Terminal
```

### Step 5: Run the Program

Enter:

```text
python main.py
```

Press **Enter**.

The Student Feedback Management System menu will appear.

---

## 🧪 Example of Student Feedback

A student can submit feedback with ratings such as:

```text
Teacher Quality      : 4
Content Quality      : 5
Doubt Clarification  : 4
Faculty Interaction  : 5
Suggestions          : More practical examples
```

The feedback is stored in:

```text
feedback.csv
```

---

## 🧪 Example of Advisor Feedback

A student can submit advisor feedback such as:

```text
Academic Guidance    : 5
Availability         : 4
Communication        : 5
Student Support      : 5
Comments             : Helpful and supportive
```

The feedback is stored in:

```text
advisor_feedback.csv
```

---

## 📌 Important Notes

- The project is completely menu-driven.
- Data is stored permanently in CSV files.
- CSV files are created automatically when required.
- The CSV files should be kept in the same folder as `main.py`.
- The program can be run using Python in Visual Studio Code.
- Feedback ratings are based on a scale of 1 to 5.
- The system provides search and feedback analysis features.

---

## 🚀 Future Improvements

Possible future improvements include:

- Add a graphical user interface (GUI)
- Add login and authentication
- Add password protection
- Add email validation
- Add duplicate student ID checking
- Generate feedback reports
- Export statistics to Excel
- Add charts and graphs
- Add database support using MySQL
- Add an admin dashboard
- Add student and faculty login systems

---

## 🎓 Learning Outcomes

This project provides practical experience with:

- Python programming
- Variables and data types
- Conditional statements
- Loops
- Functions
- File handling
- CSV file handling
- Lists and dictionaries
- Searching records
- Input validation
- Calculations
- Menu-driven programming
- Basic data analysis

---

## 👩‍💻 Author

**Aditi Jain**

**B.Tech CSE with AI & ML**  
**VIT Bhopal University**

---

## 📜 Conclusion

The **Student Feedback Management System** provides a simple way to manage student information, subjects, advisors, student feedback, and advisor feedback using Python and CSV files.

The project demonstrates the practical application of Python concepts such as functions, loops, conditional statements, file handling, CSV operations, searching, input validation, calculations, and basic feedback analysis.

The system provides a structured way to collect, store, search, and analyze feedback data through a simple menu-driven interface.