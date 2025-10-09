class Book:
    def __init__(self, title, author, is_checked_out= False):
        self.title = title
        self.author = author
        self._is_checked_out = is_checked_out

    def check_out(self):
        #Sets a book as checked out.
        self._is_checked_out = True

    def return_book(self):
        #Sets a book as available.
        self._is_checked_out = False

    def is_available(self):
        #Checks if a book is available.
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        #Adds a Book instance to the library.
        self._books.append(book)

    def check_out_book(self, title):
        #Checks out a book by title if available.
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return f'You have checked out "{title}".'
        return f'"{title}" is not available.'

    def return_book(self, title):
        #Returns a checked-out book by title.
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return f'You have returned "{title}".'
        return f'"{title}" was not checked out.'

    def list_available_books(self):
        #Lists all available books in the library.
        available = [f'{book.title} by {book.author}' for book in self._books if book.is_available()]
        return available if available else ["No books available."]
