class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)


book1 = Book("Python", "Javeria")
book2 = Book("Java", "Areesha")
book3 = Book("C++", "Areeba")

book1.display_info()
book2.display_info()
book3.display_info()