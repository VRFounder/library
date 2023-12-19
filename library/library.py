from .book import Book


class Library:
    def __init__(self):
        self.borrowers = []
        self.books = [
            Book('To Kill a Mockingbird', 'Harper Lee', 'American Literature'),
            Book('1984', 'George Orwell', 'Dystopian Fiction'),
            Book('The Great Gatsby', 'F. Scott Fitzgerald', 'American Literature'),
            Book('Pride and Prejudice', 'Jane Austen', 'British Literature'),
            Book('The Hobbit', 'J.R.R. Tolkien', 'Fantasy'),
            Book('War and Peace', 'Leo Tolstoy', 'Russian Literature'),
            Book('The Catcher in the Rye', 'J.D. Salinger', 'American Literature'),
            Book('Moby-Dick', 'Herman Melville', 'American Literature'),
            Book('Jane Eyre', 'Charlotte Bronte', 'British Literature'),
            Book('The Lord of the Rings', 'J.R.R. Tolkien', 'Fantasy'),
            Book('Crime and Punishment', 'Fyodor Dostoevsky', 'Russian Literature'),
            Book('Wuthering Heights', 'Emily Bronte', 'British Literature'),
            Book('The Odyssey', 'Homer', 'Greek Literature'),
            Book('Ulysses', 'James Joyce', 'Irish Literature'),
            Book('Madame Bovary', 'Gustave Flaubert', 'French Literature'),
            Book('The Iliad', 'Homer', 'Greek Literature'),
            Book('Don Quixote', 'Miguel de Cervantes', 'Spanish Literature'),
            Book('In Search of Lost Time', 'Marcel Proust', 'French Literature'),
            Book('Hamlet', 'William Shakespeare', 'British Literature'),
            Book('The Divine Comedy', 'Dante Alighieri', 'Italian Literature'),
        ]

        self.lent_books = {}  # format: {book: borrower}

    def add_book(self, book):
        self.books.append(book)

    def edit_book(self, book, new_book):
        index = self.books.index(book)
        self.books[index] = new_book

    def delete_book(self, book):
        self.books.remove(book)

    def search_book(self, query, by='title'):
        if by == 'title':
            books_found = [book for book in self.books if book.title == query]
        elif by == 'author':
            books_found = [book for book in self.books if book.author == query]
        elif by == 'genre':
            books_found = [book for book in self.books if book.genre == query]
        else:
            return []
        return books_found

    def sort_books(self):
        self.books.sort()

    def checkout_book(self, book, borrower):
        if book in self.books:
            self.books.remove(book)
            self.lent_books[borrower] = book
            borrower.borrowed_books.append(book)
        else:
            return 'Book is not available in the library.'

    def return_book(self, book, borrower):
        if borrower in self.lent_books and self.lent_books[borrower] == book:
            del self.lent_books[borrower]
            self.books.append(book)
            borrower.borrowed_books.append(book)
        else:
            return 'Borrower did not checkout this book.'

    def search_borrower(self, name):
        return [borrower for borrower in self.borrowers if borrower.name == name]

    def add_borrower(self, borrower):
        self.borrowers.append(borrower)

    def summary(self):
        return 'Total books: ', len(self.books), 'Lent out: ', len(self.lent_books)



