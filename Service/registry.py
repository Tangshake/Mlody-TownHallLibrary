class CheckoutRegistry:
    def __init__(self):
        self.checkout_list = []

    def add(self, entry):
        if entry is not None:
            self.checkout_list.append(entry)

    def remove(self, isbn):
        if isbn is not None:
            for i, checkout in enumerate(self.checkout_list):
                if checkout.isbn == isbn:
                    del self.checkout_list[i]
                    break

    def check_by_user(self, user_name):
        if user_name is not None:
            return any(obj.user == user_name for obj in self.checkout_list)

    def check_by_isbn(self, isbn):
        if isbn is not None:
            return any(obj.isbn == isbn for obj in self.checkout_list)

    def print_user_checkouts(self, user_name):
        if user_name:
            for checkout in self.checkout_list:
                if checkout.user == user_name:
                    print("User {} checked out the book {} ".format(checkout.user, checkout.isbn))

    def print_all_checkouts(self):
        if len(self.checkout_list) == 0:
            print("All the books are in the library!")
        else:
            print("Here is the list of the books that were checked out from the library:")
            for checkout in self.checkout_list:
                print("User: {} checked out the book: {}".format(checkout.user, checkout.isbn))
