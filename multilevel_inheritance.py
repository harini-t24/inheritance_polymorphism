class department:
    def getdept(self):
        self.id=input("Enter Dept ID:")
        self.name=input("Enter Name:")
class course(department):
    def getcourse(self):
        self.code=input("Enter course code:")
        self.cname=input("Enter course name:")
        self.duration=int(input("Enter duration of course(in months):"))
class student(course):
    def getdetails(self):
        self.roll_no=input("Enter roll no:")
        self.sname=input("Enter name of the student:")
        self.n=int(input("Enter no of marks:"))
        print("Enter the marks:")
        for i in range(self.n):
            self.marks=int(input())
        self.tot=0
        for i in range(self.n):
            self.tot+=self.marks
    def printdetails(self):
        print("Dept ID:",self.id)
        print("Dept Name:",self.name)
        print("Course code:",self.code)
        print("Course Name:",self.cname)
        print("Course Duration:",self.duration)
        print("Roll No:",self.roll_no)
        print("Student Name:",self.sname)
        print("Student Total:",self.tot)
s=student()
s.getdept()
s.getcourse()
s.getdetails()
s.printdetails()
