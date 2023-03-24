#......................................................................4

class  People:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname

    def get_email(self):
        print( f"თქვენი მეილი არის: {self.firstname}.{self.lastname}.uni@btu.edu.ge")

class Lecturer(People):
    def __init__(self,firstname,lastname,salary):
        People.__init__(self,firstname,lastname)
        self.salary = salary


    def get_email(self):
        print( f"\nთქვენი მეილი არის: {self.firstname}.{self.lastname}@btu.edu.ge")
        print(f"თქვენი ხელფასი არის: {self.salary} ₾")


class Student(People):
    def __init__(self,firstname,lastname, courses):
        People.__init__(self, firstname, lastname)
        self.courses = courses
        self.courses=[input("პირველი ლექცია: "), input("მეორე ლექცია: "), input("მესამე ლექცია: ")]

    def get_email(self):
        print( f"თქვენი მეილი არის: {self.firstname}.{self.lastname}.1@btu.edu.ge")
        print(f"tqveni leqciebia:{self.courses}")


class Doctoral_student(People):
    def __init__(self, firstname, lastname, courses, salary):
        People.__init__(self,firstname, lastname)
        self.courses = courses
        self.courses = [input("პირველი ლექცია: "), input("მეორე ლექცია: "), input("მესამე ლექცია: ")]
        self.salary = salary

    def get_email(self):
        print(f"თქვენი მეილი არის: {self.firstname}.{self.lastname}.@btu.edu.ge")
        print(f" ხელფასი არის: {self.salary}")
        print(f"თქვენი კურსებია: {self.courses}")



p1=People("luka","ivaniadze")
p1.get_email()
l1=Lecturer("davit","natroshvili",999999)
l1.get_email()
s1=Student("giorgi","dzindzibadze","leqciebi")
s1.get_email()
ds1=Doctoral_student("giurza","tugushi",'' ,95959595955)
ds1.get_email()



