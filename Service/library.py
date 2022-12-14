import copy
from Service.registry import CheckoutRegistry
from Model.checkout import Checkout
from Model.user import User


class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.checkouts = CheckoutRegistry()

    def import_books(self, new_books):
        self.books = copy.deepcopy(new_books)

    def import_users(self, new_users):
        self.users = copy.deepcopy(new_users)

    def add_book(self, book):
        if book is not None:
            self.books.append(book)

    def remove_book(self, book):
        if book is not None and book in self.books:
            self.books.remove(book)

    def update_book_pegi(self, isbn, pegi):
        if isbn and pegi:   # Check for empty string not a whitespaces
            if not self.checkouts.check_by_isbn(isbn):  # It's forbidden to update the book that is not in the library
                for i, book in enumerate(self.books):
                    if book.isbn == isbn:
                        book.pegi = pegi

    def add_user(self, user):
        if user is not None:
            self.users.append(user)

    def remove_user(self, name):
        if name:   # Check for empty string not a whitespaces
            for i, user in enumerate(self.users):
                if user.name == name:
                    del self.users[i]
                    break

    def get_user(self, name):
        return next((user for user in self.users if user.name == name), None)

    def print_all_books(self):
        print("Witaj przyjacielu. Oto lista dostępnych książek:")
        for book in self.books:
            print("Author: {} ISBN: {} PEGI: {}".format(book.author, book.isbn, book.pegi))

    def checkout_book(self, isbn, user):
        if isbn and user:   # Check for empty string not a whitespaces
            if not self.checkouts.check_by_isbn(isbn):
                checkout = Checkout(isbn, user)
                self.checkouts.add(checkout)

    def return_book(self, isbn, user):
        if isbn and user:   # Check for empty string not a whitespaces
            self.checkouts.remove(isbn)

    def print_checkouts_by_user(self, user):
        if user is not None:
            self.checkouts.print_user_checkouts(user)

    def print_all_checkouts(self):
        self.checkouts.print_all_checkouts()
