class Library:
    def __init__(self):
        self.noofbooks=0
        self.books=[]
    def addbooks(self,books):
        self.books.append(books)
        self.noofbooks=len(self.books)
    def showinfo(self):
        print(f"Library has {self.noofbooks} books")
l=Library()
l.addbooks("Harry Potter")
l.addbooks("11 rules of life")
l.showinfo()

