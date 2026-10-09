import curses

def get_string_input(stdscr, prompt):
    stdscr.addstr(prompt)
    curses.echo()
    user_input = stdscr.getstr().decode('utf-8').strip()
    curses.noecho()
    return user_input
