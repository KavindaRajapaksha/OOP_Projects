class OnlineCourse:
    def __init__(self,course,instructor):
        self.course = course
        self.instructor = instructor
        self.students = []
    def enroll_students(self,student):
        self.students.append(student)
        print(f"{student} has been enrolled in {self.course} course") # f-string use to format the string
    def course_details(self):
        print(f"Course: {self.course}")
        print(f"Instructor: {self.instructor}")
        print("Students:")
        for student in self.students:
            print(student)
    def completed_course(self,student):
        if student in self.students:
            self.students.remove(student)
            print(f"{student} has completed the course")
        else:
            print(f"{student} is not enrolled in the course")
    def average_grade(self,grades):
        total =sum(grades)
        average= total/len(grades)
        print(f"Average grade of the students is {average}")

        
course_name=input("Enter the course name: ").lower()
instructor_name=input("Enter the instructor name: ").lower()
student_name=input("Enter the student name: ").lower()

# course1 = OnlineCourse("Python Programming","John Doe")
# course1.enroll_students("Alice")
# course1.enroll_students("Bob")
# course1.enroll_students("Charlie")
# course1.course_details()
# course1.completed_course("Bob")
# course1.average_grade([90,80,70])

course2 = OnlineCourse(course_name,instructor_name)
course2.enroll_students(student_name)
course2.course_details()
course2.completed_course(student_name)
course2.average_grade([90,80,70])

