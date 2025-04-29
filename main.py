class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def __str__(self):
        return f"{self.title} by {self.author} ({self.genre})"

class User:
    def __init__(self, name):
        self.name = name
        self.checked_out_books = []

    def checkout_book(self, book):
        self.checked_out_books.append(book)

    def return_book(self, book):
        self.checked_out_books.remove(book)

class Library:
    def __init__(self):
        self.inventory = []
        self.checked_out_books = []

    def add_book(self, book):
        self.inventory.append(book)

    def checkout_book(self, user, book):
        if book in self.inventory:
            self.inventory.remove(book)
            self.checked_out_books.append(book)
            user.checkout_book(book)
            print(f"{user.name} checked out {book}")
        else:
            print(f"Sorry, {book} is not available.")

    def return_book(self, user, book):
        if book in user.checked_out_books:
            user.return_book(book)
            self.inventory.append(book)
            self.checked_out_books.remove(book)
            print(f"{user.name} returned {book}")
        else:
            print(f"{user.name} does not have {book}")

    def search_by_genre(self, genre):
        matches = [book for book in self.inventory if book.genre == genre]
        for book in matches:
            print(book)

# Example usage (test after you implement everything)
if __name__ == "__main__":
    library = Library()
    book1 = Book("Python 101", "Jane Doe", "Tech")
    book2 = Book("Learning AI", "John Smith", "Tech")
    book3 = Book("Great Expectations", "Charles Dickens", "Fiction")

    user = User("Roshan")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    library.search_by_genre("Tech")
    library.checkout_book(user, book1)
    library.return_book(user, book1)
