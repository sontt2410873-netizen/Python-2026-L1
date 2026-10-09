import os
import zipfile
from domains.models import Student, Course

def save_data(system):
    with open("students.txt", "w", encoding="utf-8") as f:
        for s in system.get_students():
            f.write(f"{s.get_id()},{s.get_name()},{s.get_dob()},{s.get_gpa()}\n")

    with open("courses.txt", "w", encoding="utf-8") as f:
        for c in system.get_courses():
            f.write(f"{c.get_id()},{c.get_name()},{c.get_credits()}\n")

    with open("marks.txt", "w", encoding="utf-8") as f:
        for c_id, student_marks in system.get_marks().items():
            for s_id, mark in student_marks.items():
                f.write(f"{c_id},{s_id},{mark}\n")

    with zipfile.ZipFile("students.dat", "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write("students.txt")
        zf.write("courses.txt")
        zf.write("marks.txt")
        
    for file in ["students.txt", "courses.txt", "marks.txt"]:
        if os.path.exists(file):
            os.remove(file)

def load_data(system):
    if not os.path.exists("students.dat"):
        return 

    with zipfile.ZipFile("students.dat", "r") as zf:
        zf.extractall()

    if os.path.exists("students.txt"):
        with open("students.txt", "r", encoding="utf-8") as f:
            for line in f:
                data = line.strip().split(',')
                if len(data) == 4:
                    student = Student(data[0], data[1], data[2])
                    student.set_gpa(float(data[3]))
                    system.add_student(student)

    if os.path.exists("courses.txt"):
        with open("courses.txt", "r", encoding="utf-8") as f:
            for line in f:
                data = line.strip().split(',')
                if len(data) == 3:
                    system.add_course(Course(data[0], data[1], int(data[2])))

    if os.path.exists("marks.txt"):
        with open("marks.txt", "r", encoding="utf-8") as f:
            for line in f:
                data = line.strip().split(',')
                if len(data) == 3:
                    system.add_mark(data[0], data[1], float(data[2]))

    for file in ["students.txt", "courses.txt", "marks.txt"]:
        if os.path.exists(file):
            os.remove(file)
