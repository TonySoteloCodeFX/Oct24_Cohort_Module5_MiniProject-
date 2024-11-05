from helpers import clr, hr
from art import main_book_menu
import user_mod
from author_mod import Author

class Book:
    book_library = []

    def __init__(self, title, author, genre, publication_date):
        '''Creates new book and adds it to book library.'''
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date
        self.availability = True
        Book.book_library.append(self)

    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def get_genre(self):
        return self.genre
    
    def get_publication_date(self):
        return self.publication_date

    def get_availability(self):
        return self.availability
    
    def switch_availability(self):
        if self.availability == True:
            self.availability = False
        else:
            self.availability = True

    @classmethod
    def display_all_books(cls):
        clr()
        hr(50)
        print("Books In Library")
        for book in cls.book_library:
            hr(50)
            print(f"Title: {book.get_title()}")
            print(f"Author: {book.get_author()}")

# ==================== ***** Functions ***** ====================

def add_book():
    '''Creates new book and prints confirmation.'''
    clr()
    hr(50)
    try:
        title = input("Enter Title: ")
        author_name = input("Enter Author: ")

        author_data = None
        for author in Author.authors:
            if author.get_author_name() == author_name:
                author_data = author
                break

        if not author_data:
            biography = input("Enter Biography: ")
            author_data = Author(author_name, biography)

        genre = input("Enter Genre: ")
        publication_date = input("Enter Publication Date: ")

        new_book = Book(title, author_data, genre, publication_date)
        clr()
        hr(50)
        print(f'{new_book.title}: by {new_book.author},\nhas been added to your library.')
    except ValueError:
        clr()
        hr(50)
        print("Input is invalid. Try again.")

def display_books():
    Book.display_all_books()

def borrow_book():
    clr()
    hr(50)
    user_name = input("Enter Your Name: ")
    borrowing_user = None
    for user in user_mod.User.users:
        if user.get_user_name() == user_name:
            borrowing_user = user
            break
    if not borrowing_user:
        print("User not found.")
        return
    
    borrow_title = input("Enter Title: ")
    book_to_borrow = None
    for book in Book.book_library:
        if book.get_title() == borrow_title:
            book_to_borrow = book
            break

    if book_to_borrow:
        if book_to_borrow.get_availability() == True:
            clr()
            hr(50)
            print("Thank you!")
            print(f"You have now borrowed: {book_to_borrow.get_title()}.")
            book_to_borrow.switch_availability()
            borrowing_user.book_list.append(book_to_borrow)
        else:
            clr()
            hr(50)
            print(f"Sorry, {borrow_title} is currently unavailable.")
    else:
        clr()
        hr(50)
        print(f"{borrow_title} not found in the library.")

def return_book():
    clr()
    hr(50)

    user_name = input("Enter Your Name: " )
    returning_user = None
    for user in user_mod.User.users:
        if user.get_user_name() == user_name:
            returning_user = user
            break
    if not returning_user:
        print("User not found.")
        return
    
    return_title = input("Enter Title: ")
    book_to_return = None
    for book in Book.book_library:
        if book.get_title() == return_title:
            book_to_return = book
            break

    if book_to_return:
        if book_to_return.get_availability() == False:
            clr()
            hr(50)
            print("Thank you!")
            print(f"You have now returned: {book_to_return.get_title()}.")
            book_to_return.switch_availability()

            if book_to_return in returning_user.book_list:
                returning_user.book_list.remove(book_to_return)
        else:
            clr()
            hr(50)
            print(f"Sorry, {return_title} was never borrowed.")
    else:
        clr()
        hr(50)
        print(f"{return_title} not found in the library.")

def search_book():
    clr()
    hr(50)
    lookup_title = input("Enter Title: ")

    book_to_lookup = None
    for book in Book.book_library:
        if book.get_title() == lookup_title:
            book_to_lookup = book
            break
    clr()
    hr(50)
    print(f"Title: {book_to_lookup.get_title()}")
    print(f"Author: {book_to_lookup.get_author()}")
    print(f"Genre: {book_to_lookup.get_genre()}")
    print(f"Publication Date: {book_to_lookup.get_publication_date()}")
    if book_to_lookup.get_availability() == True:
        print("Availability: Available Now")
    else:
        print("Availability: Not Available")

def book_menu():
    clr()
    hr(50)
    book_ops_menu = True
    while book_ops_menu:
        try:
            print(main_book_menu)
            print('''
    Book Menu:
            1. Add a new book
            2. Borrow a book
            3. Return a book
            4. Search for a book
            5. Display all books
            6. Return to main menu
                  ''')
            book_operation = int(input("Enter Number: "))

            if book_operation == 1:
                add_book()
            elif book_operation == 2:
                borrow_book()
            elif book_operation == 3:
                return_book()
            elif book_operation == 4:
                search_book()
            elif book_operation == 5:
                display_books()
            elif book_operation == 6:
                clr()
                hr(50)
                book_ops_menu = False
            else:
                clr()
                hr(50)
                print(f"{book_operation} is not an option. Try again.")
        except ValueError:
            clr()
            hr(50)
            print("Input must be a number between 1-6")