#......................................................................2

class LibraryItem():
    def __init__(self,title,subject,status):
        self.title=title
        self.subject=subject
        self.status=status

    def booking(self):
        if self.status== 0:
            print(f"თქვენ წარმატებით დაჯავშნეთ {self.title}")
        elif self.status==1:
            print("წიგნი უკვე დაჯავშნილია")
        else:
            print("წიგნი ვერ მოიძებნა")


class Book(LibraryItem):
    def __init__(self,ISBN,authors,title,subject,status):
        LibraryItem.__init__(self, title, subject, status)
        self.ISBN = ISBN
        self.authors = authors



    def booking(self):
        if self.status == 0:
            print(f"თქვენ წარმატებით დაჯავშნეთ {self.title},ავტორი: {self.authors},ISBN: {self.ISBN}")
        elif self.status == 1:
            print(f"წიგნი ,რომლის ISBN არის {self.ISBN} უკვე დაჯავშნილია")
        else:
            print("წიგნი ვერ მოიძებნა")



b1=LibraryItem("ვეფხისტყაოსანი","ლიტერატურა",0)
b1.booking()
b2=Book(123456789,"ლუკა ივანიაძე","საქართველოს ისტორია","სკოლის წიგნი",0)
b2.booking()
b3=Book(987654321,"ვეფხვაძე","კალკულუს 1","მათემატიკა",1)
b3.booking()


#class magazine იგივე პრინციპით დაიწერება, დროის უქონლობის გამო ვერ ვასწრებ(ბოდიშით წინასწარ)