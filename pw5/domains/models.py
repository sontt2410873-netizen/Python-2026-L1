import math
import numpy as np

class Student:
    def __init__(self, s_id, name, dob):
        self.__id = s_id
        self.__name = name
        self.__dob = dob
        self.__gpa = 0.0

    def get_id(self): return self.__id
    def get_name(self): return self.__name
    def get_dob(self): return self.__dob
    def get_gpa(self): return self.__gpa
    def set_gpa(self, gpa): self.__gpa = gpa


class Course:
    def __init__(self, c_id, name, credits):
        self.__id = c_id
        self.__name = name
        self.__credits = credits

    def get_id(self): return self.__id
    def get_name(self): return self.__name
    def get_credits(self): return self.__credits


class MarkManagement:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}

    def add_student(self, student): self.__students.append(student)
    def add_course(self, course): self.__courses.append(course)

    def add_mark(self, course_id, student_id, mark):
        if course_id not in self.__marks:
            self.__marks[course_id] = {}
        self.__marks[course_id][student_id] = math.floor(mark * 10) / 10

    def get_students(self): return self.__students
    def get_courses(self): return self.__courses
    def get_marks(self): return self.__marks

    def calculate_gpa_and_sort(self):
        for student in self.__students:
            s_marks, s_credits = [], []
            for course in self.__courses:
                c_id = course.get_id()
                if c_id in self.__marks and student.get_id() in self.__marks[c_id]:
                    s_marks.append(self.__marks[c_id][student.get_id()])
                    s_credits.append(course.get_credits())
            
            if s_credits:
                gpa = np.sum(np.array(s_marks) * np.array(s_credits)) / np.sum(np.array(s_credits))
                student.set_gpa(math.floor(gpa * 10) / 10)
            else:
                student.set_gpa(0.0)

        self.__students.sort(key=lambda s: s.get_gpa(), reverse=True)
