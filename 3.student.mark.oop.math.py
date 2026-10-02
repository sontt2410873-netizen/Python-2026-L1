import math
import numpy as np
import curses


class Student:
    def __init__(self, student_id, name, dob):
        self.__id = student_id
        self.__name = name
        self.__dob = dob
        self.__gpa = 0.0

    def get_id(self): return self.__id
    def get_name(self): return self.__name
    def get_dob(self): return self.__dob
    def get_gpa(self): return self.__gpa
    def set_gpa(self, gpa): self.__gpa = gpa

    def __str__(self):
        return f"ID: {self.__id:<10} | Name: {self.__name:<20} | DoB: {self.__dob:<12} | GPA: {self.__gpa:.2f}"


class Course:
    def __init__(self, course_id, name, credits):
        self.__id = course_id
        self.__name = name
        self.__credits = credits

    def get_id(self): return self.__id
    def get_name(self): return self.__name
    def get_credits(self): return self.__credits

    def __str__(self):
        return f"ID: {self.__id:<10} | Name: {self.__name:<20} | Credits: {self.__credits}"


class Mark:
    def __init__(self, student_id, course_id, mark):
        self.__student_id = student_id
        self.__course_id = course_id
        self.__mark = mark

    def get_student_id(self): return self.__student_id
    def get_course_id(self): return self.__course_id
    def get_mark(self): return self.__mark


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


def draw_menu(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 2, "==========================================", curses.A_BOLD)
    stdscr.addstr(2, 2, "    STUDENT MARK MANAGEMENT SYSTEM (PW3)  ", curses.A_BOLD)
    stdscr.addstr(3, 2, "==========================================", curses.A_BOLD)
    stdscr.addstr(5, 4, "1. Input students")
    stdscr.addstr(6, 4, "2. Input courses")
    stdscr.addstr(7, 4, "3. Input marks for a course")
    stdscr.addstr(8, 4, "4. List courses")
    stdscr.addstr(9, 4, "5. List students (Sorted by GPA Descending)")
    stdscr.addstr(10, 4, "6. Show student marks for a given course")
    stdscr.addstr(11, 4, "0. Exit")
    stdscr.addstr(13, 2, "Select an option: ")
    stdscr.refresh()


def show_courses(stdscr, courses):
    stdscr.clear()
    stdscr.addstr(1, 2, "--- Course List ---", curses.A_BOLD)
    if not courses:
        stdscr.addstr(3, 4, "No courses available.")
    else:
        for idx, c in enumerate(courses):
            stdscr.addstr(3 + idx, 4, str(c))
    stdscr.addstr(5 + len(courses), 2, "Press any key to return...")
    stdscr.refresh()
    stdscr.getch()


def show_students(stdscr, students):
    stdscr.clear()
    stdscr.addstr(1, 2, "--- Student List (Sorted by GPA Descending) ---", curses.A_BOLD)
    if not students:
        stdscr.addstr(3, 4, "No students available.")
    else:
        for idx, s in enumerate(students):
            stdscr.addstr(3 + idx, 4, str(s))
    stdscr.addstr(5 + len(students), 2, "Press any key to return...")
    stdscr.refresh()
    stdscr.getch()


def show_marks(stdscr, students, courses, marks, course_id):
    stdscr.clear()
    course = next((c for c in courses if c.get_id() == course_id), None)
    if not course:
        stdscr.addstr(1, 2, "Course not found! Press any key...")
        stdscr.getch()
        return

    stdscr.addstr(1, 2, f"--- Marks for Course: {course.get_name()} ---", curses.A_BOLD)
    for idx, s in enumerate(students):
        mark_obj = next((m for m in marks if m.get_student_id() == s.get_id() and m.get_course_id() == course_id), None)
        mark_val = f"{mark_obj.get_mark():.1f}" if mark_obj else "N/A"
        stdscr.addstr(3 + idx, 4, f"Student: {s.get_name():<20} ({s.get_id()}) | Mark: {mark_val}")

    stdscr.addstr(5 + len(students), 2, "Press any key to return...")
    stdscr.refresh()
    stdscr.getch()


def calculate_gpa(students, courses, marks):
    for s in students:
        s_marks = []
        s_credits = []
        for m in marks:
            if m.get_student_id() == s.get_id():
                course = next((c for c in courses if c.get_id() == m.get_course_id()), None)
                if course:
                    s_marks.append(m.get_mark())
                    s_credits.append(course.get_credits())

        if s_marks and sum(s_credits) > 0:
            marks_arr = np.array(s_marks)
            credits_arr = np.array(s_credits)
            gpa = np.sum(marks_arr * credits_arr) / np.sum(credits_arr)
            s.set_gpa(float(gpa))
        else:
            s.set_gpa(0.0)


def sort_students_by_gpa(students, courses, marks):
    calculate_gpa(students, courses, marks)
    students.sort(key=lambda s: s.get_gpa(), reverse=True)


def run_app(stdscr, students, courses, marks):
    curses.curs_set(1)
    while True:
        draw_menu(stdscr)
        choice = get_input(stdscr, 13, 20, "")

        if choice == '1':
            students.extend(input_students(stdscr))
        elif choice == '2':
            courses.extend(input_courses(stdscr))
        elif choice == '3':
            input_marks(stdscr, students, courses, marks)
        elif choice == '4':
            show_courses(stdscr, courses)
        elif choice == '5':
            sort_students_by_gpa(students, courses, marks)
            show_students(stdscr, students)
        elif choice == '6':
            stdscr.clear()
            c_id = get_input(stdscr, 1, 2, "Enter Course ID to view marks: ")
            show_marks(stdscr, students, courses, marks, c_id)
        elif choice == '0':
            break


if __name__ == "__main__":
    student_list = []
    course_list = []
    mark_list = []

    try:
        curses.wrapper(run_app, student_list, course_list, mark_list)
    except KeyboardInterrupt:
        print("\nProgram exited safely.")
