class Borrower:
    id_counter = 1

    def __init__(self, name):
        self.id = Borrower.id_counter
        Borrower.id_counter += 1
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
