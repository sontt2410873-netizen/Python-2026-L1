students = []   
courses = []    
marks = {}     

def input_number_of_students():
    num = int(input("Enter the number of students: "))
    return num

def input_student_info(num_students):
    for i in range(num_students):
        print(f"\n Entering information for student {i+1}:")
        student_id = input("Student ID: ")
        student_name = input("Student Name: ")
        student_dob = input("Date of Birth (DoB): ")
        
        students.append({"id": student_id, "name": student_name, "dob": student_dob})

def input_number_of_courses():
    num = int(input("\nEnter the number of courses: "))
    return num

def input_course_info(num_courses):
    for i in range(num_courses):
        print(f"\n Entering information for course {i+1}:")
        course_id = input("Course ID: ")
        course_name = input("Course Name: ")
        
        courses.append({"id": course_id, "name": course_name})

def input_marks_for_course():
    if not courses or not students:
        print("\nPlease input students and courses information first.")
        return

    course_id = input("\nEnter the Course ID to input marks: ")

    course_exists = False
    for course in courses:
        if course['id'] == course_id:
            course_exists = True
            break
            
    if not course_exists:
        print(" Course ID not found. Please try again.")
        return

    print(f"\n Inputting marks for course: {course_id} :")
    marks[course_id] = {} 
    for student in students:
        mark = float(input(f"Enter mark for student {student['name']} (ID: {student['id']}): "))
        marks[course_id][student['id']] = mark

def list_courses():
    print("\n=== LIST OF COURSES ===")
    for course in courses:
        print(f"ID: {course['id']} | Name: {course['name']}")

def list_students():
    print("\n=== LIST OF STUDENTS ===")
    for student in students:
        print(f"ID: {student['id']} | Name: {student['name']} | DoB: {student['dob']}")

def show_student_marks():
    course_id = input("\nEnter the Course ID to show marks: ")
    
    if course_id in marks:
        print(f"\n=== MARKS FOR COURSE: {course_id} ===")
        for student_id, mark in marks[course_id].items():
            student_name = "Unknown"
            for student in students:
                if student['id'] == student_id:
                    student_name = student['name']
                    break
            print(f"Student ID: {student_id} | Name: {student_name} | Mark: {mark}")
    else:
        print("\nNo marks found for this course or course does not exist.")
if __name__ == "__main__":
    while True:
        print("\n" + "="*40)
        print("      STUDENT MARK MANAGEMENT SYSTEM      ")
        print("="*40)
        print("1. Input number of students and their info")
        print("2. Input number of courses and their info")
        print("3. Input marks for a course")
        print("4. List all students")
        print("5. List all courses")
        print("6. Show student marks for a given course")
        print("0. Exit")
        
        choice = input("\nEnter your choice (0-6): ")
        
        if choice == "1":
            num = input_number_of_students()
            input_student_info(num)
        elif choice == "2":
            num = input_number_of_courses()
            input_course_info(num)
        elif choice == "3":
            input_marks_for_course()
        elif choice == "4":
            list_students()
        elif choice == "5":
            list_courses()
        elif choice == "6":
            show_student_marks()
        elif choice == "0":
            print("\nExiting program... Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select a number from 0 to 6.")