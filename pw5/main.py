import curses
from domains.models import MarkManagement, Student, Course
from input import get_string_input
import output
import persistence

def main_ui(stdscr):
    curses.cbreak()
    stdscr.keypad(True)
    system = MarkManagement()
    
    persistence.load_data(system)
    
    while True:
        output.draw_main_menu(stdscr)
        choice = get_string_input(stdscr, "Enter your choice (0-6): ")
        
        if choice == "1":
            stdscr.clear()
            output.show_message(stdscr, "--- ADD NEW STUDENT ---\n")
            s_id = get_string_input(stdscr, "Student ID: ")
            name = get_string_input(stdscr, "Student Name: ")
            dob = get_string_input(stdscr, "Date of Birth: ")
            system.add_student(Student(s_id, name, dob))
            get_string_input(stdscr, "\nSuccess! Press Enter to return...")

        elif choice == "2":
            stdscr.clear()
            output.show_message(stdscr, "--- ADD NEW COURSE ---\n")
            c_id = get_string_input(stdscr, "Course ID: ")
            name = get_string_input(stdscr, "Course Name: ")
            try:
                credits = int(get_string_input(stdscr, "Credits: "))
                system.add_course(Course(c_id, name, credits))
                get_string_input(stdscr, "\nSuccess! Press Enter to return...")
            except ValueError:
                get_string_input(stdscr, "\nInvalid credits! Press Enter...")

        elif choice == "3":
            stdscr.clear()
            output.show_message(stdscr, "--- INPUT MARKS ---\n")
            if not system.get_courses() or not system.get_students():
                get_string_input(stdscr, "Add students and courses first. Press Enter...")
                continue
                
            c_id = get_string_input(stdscr, "Enter Course ID: ")
            if not any(c.get_id() == c_id for c in system.get_courses()):
                get_string_input(stdscr, "Course not found. Press Enter to return...")
                continue
                
            for student in system.get_students():
                try:
                    mark = float(get_string_input(stdscr, f"Mark for {student.get_name()}: "))
                    system.add_mark(c_id, student.get_id(), mark)
                except ValueError:
                    output.show_message(stdscr, "Invalid mark. Skipping.\n")
                    
            get_string_input(stdscr, "\nMarks saved. Press Enter to return...")

        elif choice == "4":
            stdscr.clear()
            output.show_message(stdscr, "--- LIST OF STUDENTS ---\n")
            system.calculate_gpa_and_sort()
            for s in system.get_students():
                output.show_message(stdscr, f"ID: {s.get_id()} | Name: {s.get_name()} | GPA: {s.get_gpa()}\n")
            get_string_input(stdscr, "\nPress Enter to return...")

        elif choice == "5":
            stdscr.clear()
            output.show_message(stdscr, "--- LIST OF COURSES ---\n")
            for c in system.get_courses():
                output.show_message(stdscr, f"ID: {c.get_id()} | Name: {c.get_name()} | Credits: {c.get_credits()}\n")
            get_string_input(stdscr, "\nPress Enter to return...")

        elif choice == "6":
            stdscr.clear()
            output.show_message(stdscr, "--- SHOW MARKS ---\n")
            c_id = get_string_input(stdscr, "Enter Course ID: ")
            marks = system.get_marks()
            if c_id in marks:
                for student in system.get_students():
                    if student.get_id() in marks[c_id]:
                        output.show_message(stdscr, f"{student.get_name()}: {marks[c_id][student.get_id()]}\n")
            else:
                output.show_message(stdscr, "No marks found.\n")
            get_string_input(stdscr, "\nPress Enter to return...")

        elif choice == "0":
            stdscr.clear()
            output.show_message(stdscr, "Saving data to students.dat...\n")
            persistence.save_data(system)
            break

if __name__ == "__main__":
    curses.wrapper(main_ui)
