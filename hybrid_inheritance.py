class student:
    def get_sdetails(self):
        self.name=input("Enter name of student:")
        self.roll_no=int(input("Enter roll no:"))
        self.n=int(input("Enter number of marks:"))
        print("Enter marks:")
        for i in range(self.n):
            self.marks=int(input())
        self.tot=0
        for i in range(self.n):
            self.tot+=self.marks
    def display(self):
        print("Student name:",self.name)
        print("Student Roll no:",self.roll_no)
        print("Student Total:",self.tot)
class literary_student(student):
    def getlit_details(self):
        self.lmark=int(input("Enter marks obtained in literary association:"))
        self.tot+=self.lmark
class sports_student(student):
    def getsports_details(self):
        self.smark=int(input("Enter Sports mark:"))
        self.tot+=self.smark
class lit_sport_student(literary_student, sports_student):
    def getls_details(self):
        self.lmark=int(input("Enter marks obtained in literary association:"))
        self.smark=int(input("Enter Sports mark:"))
        self.tot+=self.lmark
        self.tot+=self.smark
print("1.Literary association\n2.Sports\n3.Both")
choice=int(input("enter choice:"))
if choice==1:
    l=literary_student()
    l.get_sdetails()
    l.getlit_details()
    l.display()
elif choice==2:
    s=sports_student()
    s.get_sdetails()
    s.getsports_details()
    s.display()
elif choice==3:
    ls=lit_sport_student()
    ls.get_sdetails()
    ls.getlit_details()
    ls.getsports_details()
    ls.display()
else:
    print("Invalid choice")

