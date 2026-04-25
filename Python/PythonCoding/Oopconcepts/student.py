class Student:
    def __init__(self, sid, sname):
        self.sid=sid
        self.sname=sname

    def display_student(self):
        print("Student ID:", self.sid)
        print("Student Name:", self.sname)