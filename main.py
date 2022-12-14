# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import Service.importer
from Service.library import Library

from Model.book import Book
from Model.user import User

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    logged_user = None

    # Create our library
    library = Library()

    # Import Books
    library.import_books(Service.importer.import_books())

    # Import users
    library.import_users(Service.importer.import_users())

    ch = 0
    for tries in range(3):
        name = input("Witaj! Podaj swoje imię: ")
        logged_user: User = library.get_user(name)
        if logged_user is not None:
            break
        else:
            print("Niestety użytkownik o takim imieniu nie ma u nas konta. Następny proszę...")

    print("Witaj {}. Co mogę dla Ciebie zrobić?".format(logged_user.name))

    action = None

    while action != "Q":
        action = input("--------- MENU ----------\n"
                       "(C) dodanie nowej książki\n"
                       "(R) odczytanie informacji o dostępnych książkach\n"
                       "(U) aktualizacja informacji o danej książce\n"
                       "(D) usuniecie książki\n"
                       "(B) wypożyczenie książki z biblioteki\n"
                       "(O) oddanie ksiażki\n"
                       "(H) założenie konta użytkownika\n"
                       "(P) pokaż wszystkie wypożyczone książki:\n"
                       "(Q) Wyjście z bliblioteki:\n"
                       "Twój Wybór:")\
                        .upper()

        if action == "C":
            print("Dodawanie nowej książki: ")
            book_name = input("Wprowadź nazwę: ")
            book_isbn = input("Wprowadź ISBN: ")
            book_pegi = input("Wprowadź PEGI: ")

            # Let's check if any of provided parameters is an empty string. This does not check white spaces!
            if book_name and book_isbn and book_pegi:
                new_book = Book(book_name, book_isbn, book_pegi)
                library.add_book(new_book)

        elif action == "R":
            library.print_all_books()

        elif action == "U":
            isbn = input("Wprowadź numer ISBN książki, którą chcesz zaktualizować: ")
            pegi = input("Wprowadź nową wartość PEGI: ")
            if isbn and pegi:
                library.update_book_pegi("123", pegi)

        elif action == "B":
            isbn = input("Wprowadź numer ISBN książki, którą chcesz wypożyczyć: ")
            if isbn:
                library.checkout_book(isbn, logged_user.name)

        elif action == "P":
            library.print_all_checkouts()

        elif action == "O":
            print("{}, którą książkę chciałbyś zwrócić?".format(logged_user.name))
            library.print_checkouts_by_user(logged_user.name)
            isbn = input("Wprowadź numer ISBN książki, którą chcesz oddać: ")
            library.return_book(isbn, logged_user.name)
