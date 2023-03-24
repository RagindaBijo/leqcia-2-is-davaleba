#......................................................................1

class  People:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname

    def get_email(self):
        print( f"თქვენი მეილი არის: {self.firstname}.{self.lastname}.uni@btu.edu.ge")

class Lecturer(People):
    def __init__(self,firstname,lastname,salary):
        People.__init__(self,firstname,lastname)
        self.salary=salary


    def get_email(self):
        print( f"\nთქვენი მეილი არის: {self.firstname}.{self.lastname}@btu.edu.ge")
        print(f"თქვენი ხელფასი არის: {self.salary} ₾")


class Student(People):
    def __init__(self,firstname,lastname,cources):
        People.__init__(self, firstname, lastname)
        self.cources = cources
        self.cources=[input("sagani1: "),input("sagani2: "),input("sagnebi3: ")]

    def get_email(self):
        print( f"თქვენი მეილი არის: {self.firstname}.{self.lastname}.1@btu.edu.ge")
        print(f"tqveni leqciebia:{self.cources}")




p1=People("luka","ivaniadze")
p1.get_email()
l1=Lecturer("davit","natroshvili",999999)
l1.get_email()
s1=Student("giorgi","dzindzibadze","leqciebi")
s1.get_email()



