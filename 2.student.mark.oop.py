class Student:
    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__dob = ""
    def input(self):
        self.__id = input("Student ID: ")
        self.__name = input("Student Name: ")
        self.__dob = input("Date of Birth (DoB): ")
    def list(self):
        print(f"ID: {self.__id} | Name: {self.__name} | DoB: {self.__dob}")

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

class Course:
    def __init__(self):
        self.__id = ""
        self.__name = ""

    def input(self):
        self.__id = input("Course ID: ")
        self.__name = input("Course Name: ")
        
    def list(self):
        print(f"ID: {self.__id} | Name: {self.__name}")

    def get_id(self):
        return self.__id


class MarkManagement:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {} 

    def add_students(self):
        num = int(input("Enter the number of students: "))
        for i in range(num):
            print(f"\n--- Entering information for student {i+1} ---")
            student = Student()
            student.input()
            self.__students.append(student)

    def add_courses(self):
        num = int(input("\nEnter the number of courses: "))
        for i in range(num):
            print(f"\nEntering information for course {i+1}")
            course = Course()
            course.input()
            self.__courses.append(course)

    def input_marks(self):
        if not self.__courses or not self.__students:
            print("\nPlease input students and courses information first.")
            return

        course_id = input("\nEnter the Course ID to input marks: ")
        
        course_exists = any(c.get_id() == course_id for c in self.__courses)
        if not course_exists:
            print("[!] Course ID not found.")
            return

        print(f"\nInputting marks for course: {course_id}")
        self.__marks[course_id] = {}
        
        for student in self.__students:
            mark = float(input(f"Enter mark for student {student.get_name()} (ID: {student.get_id()}): "))
            self.__marks[course_id][student.get_id()] = mark

    def list_all_students(self):
        print("\n=== LIST OF STUDENTS ===")
        for student in self.__students:
            student.list()

    def list_all_courses(self):
        print("\n=== LIST OF COURSES ===")
        for course in self.__courses:
            course.list()

    def show_marks(self):
        course_id = input("\nEnter the Course ID to show marks: ")
        if course_id in self.__marks:
            print(f"\n=== MARKS FOR COURSE: {course_id} ===")
            for student in self.__students:
                s_id = student.get_id()
                if s_id in self.__marks[course_id]:
                    print(f"Student ID: {s_id} | Name: {student.get_name()} | Mark: {self.__marks[course_id][s_id]}")
        else:
            print("\nNo marks found for this course.")

if __name__ == "__main__":
    system = MarkManagement()
    
    while True:
        print("\n" + "="*40)
        print("    OOP STUDENT MARK MANAGEMENT SYSTEM    ")
        print("="*40)
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List students")
        print("5. List courses")
        print("6. Show marks")
        print("0. Exit")
        
        choice = input("\nEnter your choice (0-6): ")
        
        if choice == "1":
            system.add_students()
        elif choice == "2":
            system.add_courses()
        elif choice == "3":
            system.input_marks()
        elif choice == "4":
            system.list_all_students()
        elif choice == "5":
            system.list_all_courses()
        elif choice == "6":
            system.show_marks()
        elif choice == "0":
            print("\nExiting program... Goodbye!")
            break
        else:
            print("\nInvalid choice.")