import csv
import os

# ============================================================
#          STUDENT FEEDBACK MANAGEMENT SYSTEM
# ============================================================

print("=========================================")
print("Student Feedback Management System")
print("=========================================")
print()
print("Welcome to the Student Feedback Management System!")
print("This system allows students to submit feedback,")
print("manage advisors, subjects, and ratings.")
print()


# ============================================================
#                       FILE NAMES
# ============================================================

STUDENT_FILE = "students.csv"
FEEDBACK_FILE = "feedback.csv"
ADVISOR_FILE = "advisors.csv"
SUBJECT_FILE = "subjects.csv"
ADVISOR_FEEDBACK_FILE = "advisor_feedback.csv"


# ============================================================
#                      COMMON FUNCTIONS
# ============================================================

def pause():
    input("\nPress Enter to return to the menu...")


def print_line():
    print("-" * 60)


def print_header(title):
    print()
    print("=" * 60)
    print(title.center(60))
    print("=" * 60)


def check_file(filename):
    return os.path.isfile(filename)


# ============================================================
#                    INPUT VALIDATION
# ============================================================

def get_name(message):

    while True:

        value = input(message).strip()

        if value != "":
            return value

        print("This field cannot be empty.")


def get_rating(message):

    while True:

        try:

            rating = float(input(message))

            if rating >= 1 and rating <= 5:
                return rating

            print("Please enter a rating between 1 and 5.")

        except ValueError:

            print("Please enter a valid number.")


def get_number(message):

    while True:

        try:

            number = int(input(message))

            if number > 0:
                return number

            print("Please enter a positive number.")

        except ValueError:

            print("Please enter a valid number.")


# ============================================================
#                    STUDENT MANAGEMENT
# ============================================================

def register_student():

    print_header("STUDENT REGISTRATION")

    name = get_name("Enter Student Name: ")
    student_id = get_name("Enter Student ID: ")
    course = get_name("Enter Course: ")
    branch = get_name("Enter Branch: ")
    year = get_name("Enter Year: ")
    semester = get_name("Enter Semester: ")
    email = get_name("Enter Email: ")

    file_exists = check_file(STUDENT_FILE)

    with open(STUDENT_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow([
                "Student ID",
                "Name",
                "Course",
                "Branch",
                "Year",
                "Semester",
                "Email"
            ])

        writer.writerow([
            student_id,
            name,
            course,
            branch,
            year,
            semester,
            email
        ])

    print()
    print("Student registered successfully!")

    pause()


def view_students():

    print_header("ALL REGISTERED STUDENTS")

    try:

        with open(STUDENT_FILE, "r") as file:

            reader = csv.DictReader(file)

            found = False

            for row in reader:

                found = True

                print_line()

                print("Student ID :", row["Student ID"])
                print("Name       :", row["Name"])
                print("Course     :", row["Course"])
                print("Branch     :", row["Branch"])
                print("Year       :", row["Year"])
                print("Semester   :", row["Semester"])
                print("Email      :", row["Email"])

            if not found:

                print("No students registered yet.")

    except FileNotFoundError:

        print("No students registered yet.")

    pause()


def search_student():

    print_header("SEARCH STUDENT")

    student_id = get_name("Enter Student ID: ")

    found = False

    try:

        with open(STUDENT_FILE, "r") as file:

            reader = csv.DictReader(file)

            for row in reader:

                if row["Student ID"].lower() == student_id.lower():

                    found = True

                    print()
                    print("Student Found!")
                    print_line()

                    print("Student ID :", row["Student ID"])
                    print("Name       :", row["Name"])
                    print("Course     :", row["Course"])
                    print("Branch     :", row["Branch"])
                    print("Year       :", row["Year"])
                    print("Semester   :", row["Semester"])
                    print("Email      :", row["Email"])

                    print_line()

    except FileNotFoundError:

        print("Student file does not exist.")

    if not found:

        print()
        print("No student found with this Student ID.")

    pause()


# ============================================================
#                     SUBJECT MANAGEMENT
# ============================================================

def add_subject():

    print_header("ADD SUBJECT")

    code = get_name("Enter Subject Code: ")
    subject = get_name("Enter Subject Name: ")
    faculty = get_name("Enter Faculty Name: ")
    department = get_name("Enter Department: ")
    semester = get_name("Enter Semester: ")

    file_exists = check_file(SUBJECT_FILE)

    with open(SUBJECT_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow([
                "Subject Code",
                "Subject Name",
                "Faculty",
                "Department",
                "Semester"
            ])

        writer.writerow([
            code,
            subject,
            faculty,
            department,
            semester
        ])

    print()
    print("Subject added successfully!")

    pause()


def view_subjects():

    print_header("ALL SUBJECTS")

    try:

        with open(SUBJECT_FILE, "r") as file:

            reader = csv.DictReader(file)

            found = False

            for row in reader:

                found = True

                print_line()

                print("Subject Code :", row["Subject Code"])
                print("Subject Name :", row["Subject Name"])
                print("Faculty      :", row["Faculty"])
                print("Department   :", row["Department"])
                print("Semester     :", row["Semester"])

            if not found:

                print("No subjects available.")

    except FileNotFoundError:

        print("No subjects available.")

    pause()


def search_subject():

    print_header("SEARCH SUBJECT")

    code = get_name("Enter Subject Code: ")

    found = False

    try:

        with open(SUBJECT_FILE, "r") as file:

            reader = csv.DictReader(file)

            for row in reader:

                if row["Subject Code"].lower() == code.lower():

                    found = True

                    print()
                    print("Subject Found!")
                    print_line()

                    print("Subject Code :", row["Subject Code"])
                    print("Subject Name :", row["Subject Name"])
                    print("Faculty      :", row["Faculty"])
                    print("Department   :", row["Department"])
                    print("Semester     :", row["Semester"])

                    print_line()

    except FileNotFoundError:

        print("Subject file does not exist.")

    if not found:

        print("No subject found.")

    pause()

# ============================================================
#                 ADVISOR MANAGEMENT
# ============================================================

def add_advisor():

    print_header("ADD ADVISOR")

    advisor_id = get_name("Enter Advisor ID: ")
    name = get_name("Enter Advisor Name: ")
    department = get_name("Enter Department: ")
    branch = get_name("Enter Branch: ")
    email = get_name("Enter Email: ")
    office = get_name("Enter Office Number: ")

    file_exists = check_file(ADVISOR_FILE)

    with open(ADVISOR_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow([
                "Advisor ID",
                "Name",
                "Department",
                "Branch",
                "Email",
                "Office"
            ])

        writer.writerow([
            advisor_id,
            name,
            department,
            branch,
            email,
            office
        ])

    print()
    print("Advisor added successfully!")

    pause()


def view_advisors():

    print_header("ALL ADVISORS")

    try:

        with open(ADVISOR_FILE, "r") as file:

            reader = csv.DictReader(file)

            found = False

            for row in reader:

                found = True

                print_line()

                print("Advisor ID :", row["Advisor ID"])
                print("Name       :", row["Name"])
                print("Department :", row["Department"])
                print("Branch     :", row["Branch"])
                print("Email      :", row["Email"])
                print("Office     :", row["Office"])

            if not found:

                print("No advisors available.")

    except FileNotFoundError:

        print("No advisors available.")

    pause()


def search_advisor():

    print_header("SEARCH ADVISOR")

    advisor_id = get_name("Enter Advisor ID: ")

    found = False

    try:

        with open(ADVISOR_FILE, "r") as file:

            reader = csv.DictReader(file)

            for row in reader:

                if row["Advisor ID"].lower() == advisor_id.lower():

                    found = True

                    print()
                    print("Advisor Found!")
                    print_line()

                    print("Advisor ID :", row["Advisor ID"])
                    print("Name       :", row["Name"])
                    print("Department :", row["Department"])
                    print("Branch     :", row["Branch"])
                    print("Email      :", row["Email"])
                    print("Office     :", row["Office"])

                    print_line()

    except FileNotFoundError:

        print("Advisor file does not exist.")

    if not found:

        print("No advisor found.")

    pause()


# ============================================================
#                       STUDENT FEEDBACK
# ============================================================

def submit_feedback():

    print_header("SUBMIT FEEDBACK")

    name = get_name("Enter your name: ")
    student_id = get_name("Enter Student ID: ")
    subject = get_name("Enter Subject Name: ")

    print()
    print("Please give ratings from 1 to 5.")
    print()

    teacher = get_rating("Teacher Quality (1-5): ")
    content = get_rating("Content Quality (1-5): ")
    doubts = get_rating("Doubt Clarification (1-5): ")
    interaction = get_rating("Faculty Interaction (1-5): ")

    suggestion = input("Enter your suggestions: ")

    file_exists = check_file(FEEDBACK_FILE)

    with open(FEEDBACK_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow([
                "Name",
                "Student ID",
                "Subject",
                "Teacher Quality",
                "Content Quality",
                "Doubt Clarification",
                "Faculty Interaction",
                "Suggestions"
            ])

        writer.writerow([
            name,
            student_id,
            subject,
            teacher,
            content,
            doubts,
            interaction,
            suggestion
        ])

    print()
    print("Feedback submitted successfully!")

    pause()


def view_feedback():

    print_header("ALL STUDENT FEEDBACK")

    try:

        with open(FEEDBACK_FILE, "r") as file:

            reader = csv.DictReader(file)

            found = False

            for row in reader:

                found = True

                print_line()

                print("Name                 :", row["Name"])
                print("Student ID           :", row["Student ID"])
                print("Subject              :", row["Subject"])
                print("Teacher Quality      :", row["Teacher Quality"])
                print("Content Quality      :", row["Content Quality"])
                print("Doubt Clarification  :", row["Doubt Clarification"])
                print("Faculty Interaction  :", row["Faculty Interaction"])
                print("Suggestions          :", row["Suggestions"])

            if not found:

                print("No feedback submitted yet.")

    except FileNotFoundError:

        print("No feedback has been submitted yet.")

    pause()


def search_feedback():

    print_header("SEARCH FEEDBACK")

    search_id = get_name("Enter Student ID to search: ")

    found = False

    try:

        with open(FEEDBACK_FILE, "r") as file:

            reader = csv.DictReader(file)

            for row in reader:

                if row["Student ID"].lower() == search_id.lower():

                    found = True

                    print()
                    print("Feedback Found!")
                    print_line()

                    print("Name                 :", row["Name"])
                    print("Student ID           :", row["Student ID"])
                    print("Subject              :", row["Subject"])
                    print("Teacher Quality      :", row["Teacher Quality"])
                    print("Content Quality      :", row["Content Quality"])
                    print("Doubt Clarification  :", row["Doubt Clarification"])
                    print("Faculty Interaction  :", row["Faculty Interaction"])
                    print("Suggestions          :", row["Suggestions"])

                    print_line()

    except FileNotFoundError:

        print("No feedback has been submitted yet.")

    if not found:

        print("No feedback found for the given Student ID.")

    pause()


# ============================================================
#                  SUBJECT-WISE FEEDBACK
# ============================================================

def subject_feedback():

    print_header("SUBJECT-WISE FEEDBACK")

    subject = get_name("Enter Subject Name: ")

    found = False

    try:

        with open(FEEDBACK_FILE, "r") as file:

            reader = csv.DictReader(file)

            for row in reader:

                if row["Subject"].lower() == subject.lower():

                    found = True

                    print_line()

                    print("Name                 :", row["Name"])
                    print("Student ID           :", row["Student ID"])
                    print("Subject              :", row["Subject"])
                    print("Teacher Quality      :", row["Teacher Quality"])
                    print("Content Quality      :", row["Content Quality"])
                    print("Doubt Clarification  :", row["Doubt Clarification"])
                    print("Faculty Interaction  :", row["Faculty Interaction"])
                    print("Suggestions          :", row["Suggestions"])

    except FileNotFoundError:

        print("Feedback file does not exist.")

    if not found:

        print("No feedback found for this subject.")

    pause()


# ============================================================
#                 STUDENT FEEDBACK HISTORY
# ============================================================

def feedback_history():

    print_header("STUDENT FEEDBACK HISTORY")

    student_id = get_name("Enter Student ID: ")

    found = False

    try:

        with open(FEEDBACK_FILE, "r") as file:

            reader = csv.DictReader(file)

            for row in reader:

                if row["Student ID"].lower() == student_id.lower():

                    found = True

                    print_line()

                    print("Subject             :", row["Subject"])
                    print("Teacher Quality     :", row["Teacher Quality"])
                    print("Content Quality     :", row["Content Quality"])
                    print("Doubt Clarification :", row["Doubt Clarification"])
                    print("Faculty Interaction :", row["Faculty Interaction"])
                    print("Suggestions         :", row["Suggestions"])

    except FileNotFoundError:

        print("No feedback file found.")

    if not found:

        print("No feedback history found.")

    pause()


# ============================================================
#                   AVERAGE RATING
# ============================================================

def calculate_average():

    print_header("CALCULATE AVERAGE RATING")

    total_teaching = 0
    total_content = 0
    total_doubts = 0
    total_interaction = 0
    count = 0

    try:

        with open(FEEDBACK_FILE, "r") as file:

            reader = csv.DictReader(file)

            for row in reader:

                total_teaching += float(row["Teacher Quality"])
                total_content += float(row["Content Quality"])
                total_doubts += float(row["Doubt Clarification"])
                total_interaction += float(row["Faculty Interaction"])

                count += 1

    except FileNotFoundError:

        print("No feedback has been submitted yet.")

    if count > 0:

        teacher_average = total_teaching / count
        content_average = total_content / count
        doubts_average = total_doubts / count
        interaction_average = total_interaction / count

        overall_average = (
            teacher_average
            + content_average
            + doubts_average
            + interaction_average
        ) / 4

        print()
        print("Average Ratings")
        print_line()

        print(
            "Teacher Quality      :",
            round(teacher_average, 2)
        )

        print(
            "Content Quality      :",
            round(content_average, 2)
        )

        print(
            "Doubt Clarification  :",
            round(doubts_average, 2)
        )

        print(
            "Faculty Interaction  :",
            round(interaction_average, 2)
        )

        print_line()

        print(
            "Overall Average      :",
            round(overall_average, 2)
        )

    else:

        print("No feedback available.")

    pause()


# ============================================================
#                 FEEDBACK STATISTICS
# ============================================================

def feedback_statistics():

    print_header("FEEDBACK STATISTICS")

    count = 0

    total_teacher = 0
    total_content = 0
    total_doubts = 0
    total_interaction = 0

    try:

        with open(FEEDBACK_FILE, "r") as file:

            reader = csv.DictReader(file)

            for row in reader:

                count += 1

                total_teacher += float(row["Teacher Quality"])
                total_content += float(row["Content Quality"])
                total_doubts += float(row["Doubt Clarification"])
                total_interaction += float(row["Faculty Interaction"])

    except FileNotFoundError:

        print("No feedback data available.")

    if count == 0:

        print("No feedback data available.")

    else:

        overall = (
            total_teacher
            + total_content
            + total_doubts
            + total_interaction
        ) / (count * 4)

        print()
        print("Total Feedback Records :", count)

        print()

        print(
            "Teacher Quality Average :",
            round(total_teacher / count, 2)
        )

        print(
            "Content Quality Average :",
            round(total_content / count, 2)
        )

        print(
            "Doubt Clarification Average :",
            round(total_doubts / count, 2)
        )

        print(
            "Faculty Interaction Average :",
            round(total_interaction / count, 2)
        )

        print()

        print(
            "Overall Average Rating :",
            round(overall, 2)
        )

    pause()


# ============================================================
#                    ADVISOR FEEDBACK
# ============================================================

def submit_advisor_feedback():

    print_header("SUBMIT ADVISOR FEEDBACK")

    student_name = get_name("Enter Student Name: ")
    student_id = get_name("Enter Student ID: ")
    advisor_name = get_name("Enter Advisor Name: ")

    print()
    print("Please give ratings from 1 to 5.")
    print()

    guidance = get_rating("Academic Guidance (1-5): ")
    availability = get_rating("Advisor Availability (1-5): ")
    communication = get_rating("Communication (1-5): ")
    support = get_rating("Student Support (1-5): ")

    comments = input("Enter your comments: ")

    file_exists = check_file(ADVISOR_FEEDBACK_FILE)

    with open(
        ADVISOR_FEEDBACK_FILE,
        "a",
        newline=""
    ) as file:

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow([
                "Student Name",
                "Student ID",
                "Advisor Name",
                "Academic Guidance",
                "Availability",
                "Communication",
                "Student Support",
                "Comments"
            ])

        writer.writerow([
            student_name,
            student_id,
            advisor_name,
            guidance,
            availability,
            communication,
            support,
            comments
        ])

    print()
    print("Advisor feedback submitted successfully!")

    pause()

# ============================================================
#                    MAIN MENU
# ============================================================

while True:

    print()
    print("============================================================")
    print("          STUDENT FEEDBACK MANAGEMENT SYSTEM")
    print("============================================================")

    print()
    print("--------------- STUDENT MANAGEMENT ----------------")
    print("1.  Register Student")
    print("2.  View All Students")
    print("3.  Search Student")

    print()
    print("--------------- SUBJECT MANAGEMENT ----------------")
    print("4.  Add Subject")
    print("5.  View All Subjects")
    print("6.  Search Subject")

    print()
    print("--------------- ADVISOR MANAGEMENT ----------------")
    print("7.  Add Advisor")
    print("8.  View All Advisors")
    print("9.  Search Advisor")

    print()
    print("--------------- FEEDBACK MANAGEMENT ----------------")
    print("10. Submit Student Feedback")
    print("11. View All Feedback")
    print("12. Search Feedback")
    print("13. Subject-wise Feedback")
    print("14. Student Feedback History")
    print("15. Calculate Average Rating")
    print("16. Feedback Statistics")

    print()
    print("--------------- ADVISOR FEEDBACK -------------------")
    print("17. Submit Advisor Feedback")

    print()
    print("18. Exit")

    print()
    choice = input("Enter your choice: ")

    if choice == "1":
        register_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        add_subject()

    elif choice == "5":
        view_subjects()

    elif choice == "6":
        search_subject()

    elif choice == "7":
        add_advisor()

    elif choice == "8":
        view_advisors()

    elif choice == "9":
        search_advisor()

    elif choice == "10":
        submit_feedback()

    elif choice == "11":
        view_feedback()

    elif choice == "12":
        search_feedback()

    elif choice == "13":
        subject_feedback()

    elif choice == "14":
        feedback_history()

    elif choice == "15":
        calculate_average()

    elif choice == "16":
        feedback_statistics()

    elif choice == "17":
        submit_advisor_feedback()

    elif choice == "18":
        print()
        print("============================================================")
        print("Thank you for using the Student Feedback Management System!")
        print("============================================================")
        break

    else:
        print()
        print("Invalid choice!")
        print("Please enter a number from 1 to 18.")