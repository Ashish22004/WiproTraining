class Teacher:
    def __init__(self,tid,tname,subject):
        self.tid=tid
        self.tname=tname
        self.subject=subject

    def display_teacher(self):
        print("Teacher ID:", self.tid)
        print("Teacher Name:",self.tname)
        print("Subject:",self.subject)