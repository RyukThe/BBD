print("Hello world!!!")

def printTable(number):
    for i in range(number, ((number*10))+1, number):
        print(i)

printTable(5)

class demo:
    def __init__(self):
        pass
    def __init__(self, num1, num2):
        self.num1=num1
        self.num2=num2

    def __init__(self, name, lastname, dateOfBirth):
        self.name=name
        self.lastname=lastname
        self.dateOfBirth=dateOfBirth

    def name(self, name=input("Please Enter Your Name: ")):
        print("Name", name)
d = demo()
d.name()