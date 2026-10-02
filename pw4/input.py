import math
import curses
from domains import Student, Course, Mark


def get_input(stdscr, row, col, prompt):
    curses.echo()
    stdscr.addstr(row, col, prompt)
    stdscr.refresh()
    val = stdscr.getstr(row, col + len(prompt), 30).decode('utf-8')
    curses.noecho()
    return val.strip()


def input_students(stdscr):
    stdscr.clear()
    students = []
    try:
        n = int(get_input(stdscr, 1, 2, "Enter number of students: "))
        for i in range(n):
            stdscr.clear()
            stdscr.addstr(1, 2, f"--- Input Student {i + 1}/{n} ---")
            s_id = get_input(stdscr, 3, 2, "Student ID: ")
            name = get_input(stdscr, 4, 2, "Student Name: ")
            dob = get_input(stdscr, 5, 2, "Date of Birth (DD/MM/YYYY): ")
            students.append(Student(s_id, name, dob))
    except ValueError:
        stdscr.addstr(7, 2, "Invalid number! Press any key to return...")
        stdscr.getch()
    return students


def input_courses(stdscr):
    stdscr.clear()
    courses = []
    try:
        n = int(get_input(stdscr, 1, 2, "Enter number of courses: "))
        for i in range(n):
            stdscr.clear()
            stdscr.addstr(1, 2, f"--- Input Course {i + 1}/{n} ---")
            c_id = get_input(stdscr, 3, 2, "Course ID: ")
            name = get_input(stdscr, 4, 2, "Course Name: ")
            credits = int(get_input(stdscr, 5, 2, "Course Credits: "))
            courses.append(Course(c_id, name, credits))
    except ValueError:
        stdscr.addstr(7, 2, "Invalid input! Press any key to return...")
        stdscr.getch()
    return courses


def input_marks(stdscr, students, courses, marks):
    stdscr.clear()
    if not students or not courses:
        stdscr.addstr(1, 2, "Please input both students and courses first! Press any key...")
        stdscr.getch()
        return

    stdscr.addstr(1, 2, "--- Available Courses ---")
    for idx, c in enumerate(courses):
        stdscr.addstr(2 + idx, 4, str(c))

    row_offset = 3 + len(courses)
    c_id = get_input(stdscr, row_offset, 2, "Enter Course ID to input marks: ")

    selected_course = next((c for c in courses if c.get_id() == c_id), None)
    if not selected_course:
        stdscr.addstr(row_offset + 2, 2, "Course not found! Press any key...")
        stdscr.getch()
        return

    stdscr.clear()
    stdscr.addstr(1, 2, f"--- Entering marks for course: {selected_course.get_name()} ---")
    for idx, s in enumerate(students):
        try:
            raw_mark = float(get_input(stdscr, 3 + idx, 2, f"Mark for {s.get_name()} ({s.get_id()}): "))
            rounded_mark = math.floor(raw_mark * 10) / 10.0
            existing = next((m for m in marks if m.get_student_id() == s.get_id() and m.get_course_id() == c_id), None)
            if existing:
                marks.remove(existing)
            marks.append(Mark(s.get_id(), c_id, rounded_mark))
        except ValueError:
            stdscr.addstr(3 + idx, 50, "Invalid mark, skipped!")
