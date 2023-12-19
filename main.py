from library.book import Book
from library.borrower import Borrower
from library.library import Library


def get_non_empty_input(prompt):
    result = input(prompt)
    while not result.strip():
        print("Input cannot be empty!")
        result = input(prompt)
    return result


def main():
    # Initialize library
    lib = Library()

    while True:
        print("\n=== Library Management System ===")
        print("1: Add book")
        print("2: Add borrower")
        print("3: Search for book")
        print("4: Search for borrower")
        print("5: Checkout book")
        print("6: Return book")
        print("7: Print summary")
        print("0: Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = get_non_empty_input("Enter book title: ")
            author = get_non_empty_input("Enter book author: ")
            genre = get_non_empty_input("Enter book genre: ")
            book = Book(title, author, genre)
            lib.add_book(book)
            print(f"Book '{book}' added to the library.")
            input("Press any key to continue...")

        elif choice == '2':
            name = get_non_empty_input("Enter borrower name: ")
            borrower = Borrower(name)
            lib.add_borrower(borrower)
            print(f"Borrower '{borrower.name}' with ID: '{borrower.id}' registered in the library.")
            input("Press any key to continue...")

        elif choice == '3':
            query = get_non_empty_input("Enter search query: ")
            by = input("Search by (title/author/genre): ")
            books_found = lib.search_book(query, by)
            if books_found:
                print("Books found:")
                for book in books_found:
                    print(book)
            else:
                print("No books found.")
            input("Press any key to continue...")

        elif choice == '4':
            name = get_non_empty_input("Enter borrower name: ")
            borrowers_found = lib.search_borrower(name)
            if borrowers_found:
                print("Borrowers found:")
                for borrower in borrowers_found:
                    print("----------------------")
                    print("Name: " + borrower.name)
                    print("ID: " + str(borrower.id))

            else:
                print("No borrowers found.")
            input("Press any key to continue...")

        elif choice == '5':
            title = get_non_empty_input("Enter book title to checkout: ")
            book = next((book for book in lib.books if book.title == title), None)
            if book:
                name = get_non_empty_input("Enter borrower name: ")
                borrower = next((borrower for borrower in lib.borrowers if borrower.name == name), None)
                if borrower:
                    lib.checkout_book(book, borrower)
                    print(f"Book '{book}' checked out to {borrower}.")
                else:
                    print("Borrower not found.")
            else:
                print("Book not found.")
            input("Press any key to continue...")

        elif choice == '6':
            title = get_non_empty_input("Enter book title to return: ")
            book = next((book for book in lib.books if book.title == title), None)
            if title in lib.lent_books.title:
                name = get_non_empty_input("Enter borrower name: ")
                borrower = next((borrower for borrower in lib.borrowers if borrower.name == name), None)
                if borrower:
                    lib.return_book(book, borrower)
                    print(f"Book '{book}' returned by {borrower}.")
                else:
                    print("Borrower not found.")
            else:
                print("Book not found.")
            input("Press any key to continue...")

        elif choice == '7':
            print(lib.summary())
            input("Press any key to continue...")

        elif choice == '0':
            break

        else:
            print("Invalid option. Please try again.")
            input("Press any key to continue...")


if __name__ == "__main__":
    main()
