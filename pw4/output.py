import curses


def draw_menu(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 2, "==========================================", curses.A_BOLD)
    stdscr.addstr(2, 2, "    STUDENT MARK MANAGEMENT SYSTEM (PW4)  ", curses.A_BOLD)
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
