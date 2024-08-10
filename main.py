from datetime import datetime

class Librarian:
    def __init__(self):
        self.membership = []
        self.shelf = [[None for _ in range(5)] for _ in range(5)]

    def addbook(self, b):
        for i in range(5):
            for j in range(5):
                if self.shelf[i][j] is None:
                    self.shelf[i][j] = b
                    return
        print("No space to add book:", b.bookname)

    def searchbook(self, b):
        for i in range(5):
            for j in range(5):
                if self.shelf[i][j] and self.shelf[i][j].bookname == b.bookname and not self.shelf[i][j].isborrowed:
                    print("SUCCESS, Found", b.bookname, "at", i, j)
                    return
        print("FAILURE", b.bookname, "not found")

    def checkout(self, user, b, date):
        for member in self.membership:
            if member.name == user.name:
                break
        else:
            print("FAILURE", user.name, "is not a registered member")
            return

        for i in range(5):
            for j in range(5):
                if self.shelf[i][j] and self.shelf[i][j].bookname == b.bookname and not self.shelf[i][j].isborrowed:
                    self.shelf[i][j].isborrowed = True
                    self.shelf[i][j].borrowername = user.name
                    member.checkedoutbooks[b.bookname] = date
                    print("SUCCESS", user.name, "borrowed", b.bookname)
                    return
        print("FAILURE", b.bookname, "is not available")

    def returnborrow(self, b, date):
        for i in range(5):
            for j in range(5):
                if self.shelf[i][j] and self.shelf[i][j].bookname == b.bookname:
                    if not self.shelf[i][j].isborrowed:
                        print("FAILURE", b.bookname, "is not a borrowed book")
                        return
                    else:
                        self.shelf[i][j].isborrowed = False
                        self.shelf[i][j].borrowername = "Nil"
                        self.calculate_fine(b, date)
                        print("SUCCESS, returned", b.bookname)
                        return
        print("FAILURE", b.bookname, "not found")

    def calculate_fine(self, b, return_date):
        return_date = datetime.strptime(return_date, "%d-%m-%Y")
        for member in self.membership:
            if b.bookname in member.checkedoutbooks:
                checkout_date = datetime.strptime(member.checkedoutbooks[b.bookname], "%d-%m-%Y")
                borrowed_days = (return_date - checkout_date).days

                if borrowed_days > 15:
                    fine = (borrowed_days - 15) * 20
                    print(f"Fine incurred for {b.bookname}: Rs.{fine}")
                del member.checkedoutbooks[b.bookname]
                break

    def register(self, user, date):
        for member in self.membership:
            if member.name == user.name:
                print("FAILURE, Already registered", user.name, date)
                return
        self.membership.append(user)
        print("SUCCESS, Registered", user.name)

    def cancel(self, user):
        for member in self.membership:
            if member.name == user.name:
                self.membership.remove(member)
                print("SUCCESS, Membership cancelled", user.name)
                return
        print("FAILURE, Not a registered member", user.name)


class Book:
    def __init__(self, bookname, isborrowed=False, borrowername="Nil"):
        self.bookname = bookname
        self.isborrowed = isborrowed
        self.borrowername = borrowername


class Member:
    def __init__(self, name, doj="Nil"):
        self.name = name
        self.doj = doj
        self.checkedoutbooks = {}
        self.reservedbooks = []


def main():
    librarian = Librarian()

    librarian.addbook(Book("Ponniyin Selvan"))
    librarian.addbook(Book("Life Of Pi"))
    librarian.addbook(Book("Naran"))

    while True:
        choice = int(input("Enter your choice: 1.Register Membership 2.Cancel Membership 3.Search and Retrieve book 4.Checkout Book 5.Return Book 6.Quit: "))
        if choice == 1:
            name = input("Enter the name: ")
            date = input("Enter joining date: ")
            user = Member(name, date)
            librarian.register(user, date)
        elif choice == 2:
            name = input("Enter the name: ")
            user = Member(name)
            librarian.cancel(user)
        elif choice == 3:
            book = input("Enter the book to search: ")
            b = Book(book)
            librarian.searchbook(b)
        elif choice == 4:
            name = input("Enter the name: ")
            book = input("Enter the book: ")
            date = input("Enter checkout date: ")
            user = Member(name)
            b = Book(book)
            librarian.checkout(user, b, date)
        elif choice == 5:
            book = input("Enter the book: ")
            date = input("Enter return date: ")
            b = Book(book)
            librarian.returnborrow(b, date)
        elif choice == 6:
            break

main()
