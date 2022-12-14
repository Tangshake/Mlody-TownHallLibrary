from Model.book import Book
from Model.user import User


def import_books():
    books = []

    # Create books
    book = Book("Koniuszy", "123", 12)
    book1 = Book("Wyrwigrosz", "456", 16)
    book2 = Book("Koniuszy", "789", 18)

    books.append(book)
    books.append(book1)
    books.append(book2)

    return books


def import_users():
    users = []

    # Create books
    user = User("Marian", 10)
    user1 = User("Bobek", 12)
    user2 = User("Sebix", 14)
    user3 = User("Onucy", 16)
    user4 = User("Barabasz", 18)

    users.append(user)
    users.append(user1)
    users.append(user2)
    users.append(user3)
    users.append(user4)

    return users


class Importer:
    pass


