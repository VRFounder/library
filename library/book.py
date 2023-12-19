class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def __str__(self):
        return "<{}> by {}".format(self.title, self.author)

    def __repr__(self):
        return "'{}' by {}".format(self.title, self.author)
