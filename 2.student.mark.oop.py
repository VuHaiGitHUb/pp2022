from typing import List

print(""" 
  ------------------------------------------------------
 |======================================================| 
 |========    Student Mark Management System	========|
 |======================================================|
  ------------------------------------------------------
  """)

STUDENTS = []
class Student:
    def __init__(self, id, name, dob):
        self._id = id
        self._name = name
        self._dob = dob

    def get_studentid(self):
        return self._id
    def set_studentid(self, id):
        self._id = id

    def get_studentname(self):
        return self._name
    def set_studentname(self, name):
        self._name = name

    def get_studentdob(self):
        return self._dob
    def set_studentdob(self, dob):
        self._dob = dob

    def __str__(self):
        return f"Students:\n - ID: {self._id}\n - Name: {self._name}\n - DOB:{self._dob}"

COURSES = []
class Course:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    def get_courseid(self):
        return self._id
    def set_studentdob(self, id):
        self._id = id

    def get_coursename(self):
        return self._name
    def set_coursename(self, name):
        self._name = name

    def __str__(self):
        return f"Courses:\n - ID: {self._id}\n - Name: {self._name}"

MARKS = []
class Mark:
    def __init__(self,student_id, mark):
        self._student_id = student_id
        self._mark = mark

    def get_student_id(self):
        return self._student_id
    def set_student_id(self, student_id):
        self._student_id = student_id

    def get_mark(self):
        return self._mark
    def set_mark(self, mark):
        self._mark = mark

def inputStudentCount():
    print("================================================")
    studentcount = int(input("Please Enter Number Of Students: "))
    return studentcount

def inputStudentInfo():
    print("Student Information")
    student_id = input("Please Enter Student ID: ")
    student_name = input("Please Enter Student Name: ")
    student_dob = input("Please Enter Student DOB: ")
    student_info = Student(student_id,student_name,student_dob)
    STUDENTS.append(student_info)

def inputCourseCount():
    print("================================================")
    coursecount = int(input("Please Enter Number of Courses: "))
    return coursecount

def inputCourseInfo():
    print("Course Information")
    course_name = input("Please Enter Course Name: ")
    course_id = input("Please Enter Course ID: ")
    course_info = Course(course_id,course_name)
    COURSES.append(course_info)

def ChooseCourse():
    print("================================================")
    print("Choose Course")
    for i in COURSES:
            CourseID = input("Please Enter a Course ID: ")
            CourseList = [course_id.get_courseid() for course_id in COURSES]
            if CourseID in CourseList:
                print("Continue...")
                break
            else:
                print("Course ID not found")

def inputMark():
    print("Mark Input System")
    for i in STUDENTS:
        StudentID = input("Please Enter a Student ID: ")
        StudentList = [student_id.get_studentid() for student_id in STUDENTS]
        if StudentID in StudentList:
            mark = float(input("Please Enter Mark: "))
            Mark_Of_A_Student = Mark(StudentID,mark)
            MARKS.append(Mark_Of_A_Student)
            break
        else:
            print ("Invalid Value")

def ListStudents():
    print("Students List:")
    for i in STUDENTS:
        print(i)

def ListCourses():
    print("Courses List:")
    for i in COURSES:
        print(i)

def ShowMarks():
    print("Mark List:")
    for i in COURSES:
        print(f"\tCourse ID: {i.get_courseid()}")
        for j in range(0,len(MARKS)):
                print(f"\nStudent ID: {MARKS[j].get_student_id()}  |  Mark: {MARKS[j].get_mark()}")

studentcount = int(inputStudentCount())
for i in range(0,studentcount):
    inputStudentInfo()
coursecount = int(inputCourseCount())
for i in range(0,coursecount):
    inputCourseInfo()
ChooseCourse()
inputMark()

while True:
    print(f'''
    ================================================================
    =======================   System Menu   ========================
    1. View Students List
    2. View Courses List
    3. View Marks List
    4. Exit 
''')
    choice = int(input("Please Enter Your Choice: "))
    if choice == 1:
        ListStudents()
    elif choice == 2:
        ListCourses()
    elif choice == 3:
        ShowMarks()
    elif choice == 4:
        break
