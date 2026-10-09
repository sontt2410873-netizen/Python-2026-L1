import curses

def draw_main_menu(stdscr):
    stdscr.clear()
    stdscr.addstr("========================================\n", curses.A_BOLD)
    stdscr.addstr("         PW5: PERSISTENT SYSTEM         \n", curses.A_BOLD)
    stdscr.addstr("========================================\n")
    stdscr.addstr("1. Input a student\n")
    stdscr.addstr("2. Input a course\n")
    stdscr.addstr("3. Input marks\n")
    stdscr.addstr("4. List students (Sorted by GPA)\n")
    stdscr.addstr("5. List courses\n")
    stdscr.addstr("6. Show marks for a course\n")
    stdscr.addstr("0. Save and Exit\n")
    stdscr.addstr("----------------------------------------\n")

def show_message(stdscr, message):
    stdscr.addstr(message)
