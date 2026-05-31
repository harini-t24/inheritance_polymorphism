class employee:
    def getdetails(self):
        self.id=input("Enter employee ID:")
        self.name=input("Enter name of employee:")
        self.salary=int(input("Enter employee salary:"))
        self.per=int(input("Enter bonus percentage:"))
    def calculate_bonus(self,allow):
        self.bonus=((self.per*0.01)*self.salary)+allow
class manager(employee):
    def manager_details(self):
        self.dept=input("Enter department of employee;")
        self.team_size=int(input("Enter team size:"))
        self.allow=int(input("Enter Allowance:"))
        self.calculate_bonus(self.allow)
        self.design="Manager"
    def print_manager(self):
        print("Employee ID:",self.id)
        print("Employee name:",self.name)
        print("Employee designation:",self.design)
        print("Employee Department:",self.dept)
        print("Employee team size:",self.team_size)
        print("Employee bonus:",self.bonus)
class developer(employee):
    def developer_details(self):
        self.project=input("Enter developer project:")
        self.experience=int(input("Enter years of experience:"))
        self.design="Developer"
        self.calculate_bonus(0)
    def print_developer(self):
        print("Employee ID:",self.id)
        print("Employee Name:",self.name)
        print("Employee designation:",self.design)
        print("Project of Employee:",self.project)
        print("Employee's Years of experience:",self.experience)
        print("Employee Bonus:",self.bonus)
print("1.Manager\n2.Developer")
choice=int(input("Enter choice:"))
if choice==1:
    m=manager()
    m.getdetails()
    m.manager_details()
    m.print_manager()
elif choice==2:
    d=developer()
    d.getdetails()
    d.developer_details()
    d.print_developer()
else:
    print('Invalid choice')
