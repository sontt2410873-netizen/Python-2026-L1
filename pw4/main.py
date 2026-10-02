import curses
import numpy as np
import input as inp
import output as out


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
        out.draw_menu(stdscr)
        choice = inp.get_input(stdscr, 13, 20, "")

        if choice == '1':
            students.extend(inp.input_students(stdscr))
        elif choice == '2':
            courses.extend(inp.input_courses(stdscr))
        elif choice == '3':
            inp.input_marks(stdscr, students, courses, marks)
        elif choice == '4':
            out.show_courses(stdscr, courses)
        elif choice == '5':
            sort_students_by_gpa(students, courses, marks)
            out.show_students(stdscr, students)
        elif choice == '6':
            stdscr.clear()
            c_id = inp.get_input(stdscr, 1, 2, "Enter Course ID to view marks: ")
            out.show_marks(stdscr, students, courses, marks, c_id)
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
