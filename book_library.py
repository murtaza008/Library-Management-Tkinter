# book_library.py
# Murtaza Mazhar
# F2022065163
# Custom exception for unavailable book lending
class BookNotAvailableError(Exception):
    pass

# Book class with basic attributes
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_lent = False

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

# Library class to manage books
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        # Check for duplicate ISBN
        if any(b.isbn == book.isbn for b in self.books):
            raise ValueError("A book with this ISBN already exists.")
        self.books.append(book)

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]

    def lend_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.is_lent:
                book.is_lent = True
                return book
        raise BookNotAvailableError("Book is either not available or already lent.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.is_lent:
                book.is_lent = False
                return
        raise BookNotAvailableError("This book was not lent out.")

    def __iter__(self):
        return (book for book in self.books if not book.is_lent)

    def books_by_author(self, author):
        return (book for book in self.books if book.author.lower() == author.lower())

# Subclass for digital libraries with download size
class EBook(Book):
    def __init__(self, title, author, isbn, download_size):
        super().__init__(title, author, isbn)
        self.download_size = download_size

    def __str__(self):
        return f"{self.title} by {self.author} (eBook, {self.download_size}MB)"
