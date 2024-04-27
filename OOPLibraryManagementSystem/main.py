class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
    
    def display_info(self):
        print(f"Title: {self.title} \nAuthor: {self.author} \nYear: {self.year}")

    
class FictionBook(Book):
    def __init__(self,title,author,year,genre):
        super().__init__(title,author,year)
        self.genre = genre

    def display_info(self):
        super().display_info()
        print(f"Genre: {self.genre}")

class NonFictionBook(Book):
    def __init__(self,title,author,year,topic):
        super().__init__(title,author,year)
        self.topic = topic

    def display_info(self):
        super().display_info()
        print(f"Topic: {self.topic}")

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self,book):
        self.books.append(book)
    
    def display_books(self):
        for book in self.books:
            book.display_info()
            print("\n")
    
    def search_author(self,author):
        found_books=[]
        for book in self.books:
            if book.author == author:
                found_books.append(book)
        if found_books:
            print(f"Books by {author}:")
            for book in found_books:
                book.display_info()
                print("\n")
        else:
            print("No books found by this author")

    def search_year(self,year):
        found_books=[]
        for book in self.books:
            if book.year == year:
                found_books.append(book)
        if found_books:
            print(f"Books from {year}:")
            for book in found_books:
                book.display_info()
                print("\n")
        else:
            print("No books found from this year")  
    
    def search_book(self,title):
        print(f"Searching for {title}:")
        for book in self.books:
            if book.title == title:
                book.display_info()
                return
        print("Book not found")

library = Library()
book1 = FictionBook("Harry Potter","J.K. Rowling",1997,"Fantasy")
book2 = FictionBook("The Lord of the Rings","J.R.R. Tolkien",1954,"Fantasy")
book3 = NonFictionBook("Sapiens","Yuval Noah Harari",2011,"History")
book4 = NonFictionBook("The Selfish Gene","Richard Dawkins",1976,"Science")



library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

library.display_books()
library.search_author("J.K. Rowling")
library.search_year(1954)
library.search_book("Sapiens")
library.search_book("The Selfish Gene")