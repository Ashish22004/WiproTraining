from student import Student

class StudentGrade(Student):
    def __init__(self, sid, sname, marks):
        super().__init__(sid, sname)
        self.marks=marks

    def calculate_grade(self):
        if self.marks >= 90:
            grade = "A"
        elif self.marks >=75:
            grade = "B"
        elif self.marks >=50:
            grade = "C"
        else:
            grade ="Fail"

        return grade

    def display_all(self):
        self.display_student()
        print("marks:", self.marks)
        print("Grade:", self.calculate_grade())

sid = int(input("Enter Student ID:"))
sname=input("Enter Student Name:")
marks=int(input("Enter Marks:"))

s=StudentGrade(sid,sname,marks)
s.display_all()