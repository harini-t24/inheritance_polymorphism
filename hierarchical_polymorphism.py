class product:
    def getdetails(self):
        self.id=input("Enter ID of product:")
        self.name=input("Enter Product Name:")
        self.price=int(input("Enter Product price:"))
    def add_to_cart(self):
        print("Product added to the cart")
    def display(self):
        print("Product ID:",self.id)
        print("Product Name:",self.name)
        print("Product price:",self.price)
class electronics(product):
    def getelectronic_details(self):
        self.ename=input("Enter product name:")
        self.ebrand=input("Enter Brand name:")
        self.ewrnty=int(input("Enter waranty period (months):"))
    def display(self):
        super().display()
        print("Product Name:",self.ename)
        print("Brand name:",self.ebrand)
        print("Warranty period:",self.ewrnty)
class clothes(product):
    def getcloth_details(self):
        self.ctype=input("Enter clothes type:")
        self.csize=int(input("Enter size of the cloth:"))
        self.color=input("Enter colour of the cloth:")
    def display(self):
        super().display()
        print("Cloth Type:",self.ctype)
        print("Cloth Size:",self.csize)
        print("Cloth Colour:",self.color)
print("1.Electronics\n2.Clothes")
choice=int(input("Enter your choice:"))
if choice==1:
    e=electronics()
    e.getdetails()
    e.getelectronic_details()
    e.add_to_cart()
    e.display()
elif choice==2:
    c=clothes()
    c.getdetails()
    c.getcloth_details()
    c.add_to_cart()
    c.display()
else:
    print("Invalid choice")


