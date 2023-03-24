#......................................................................3
class Contacts:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone


class MailSender:
    def __init__(self,email):
        self.email=email

    def send_mail(self):
        print(f"მეილი გაიგზავნა ამ მეილზე: {self.email}")

class Friend(Contacts,MailSender):
    def __init__(self,name,phone,email):
        Contacts.__init__(self,name,phone)
        MailSender.__init__(self,email)



class Family(Contacts,MailSender):
    def __init__(self,name,phone,email,birthdate):
        Contacts.__init__(self,name,phone)
        MailSender.__init__(self,email)
        self.birthdate=birthdate



fa1=Family("luka", 551003915 ,"luka.ivaniadze.2@btu.edu.ge","02.07.2003")
fa1.send_mail()
fr1=Friend('kosta',595501415,"guranduxt.gomarteli@gmail.com")
fr1.send_mail()
