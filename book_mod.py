from helpers import clr, hr
from art import main_book_menu, congrats
import user_mod
from author_mod import Author
from sql_connection import connection_to_db

class Book:

    def __init__(self, title, author, genre, publication_date):
        '''Creates new book and adds it to book library.'''
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date
        self.availability = True

    def get_title(self):
        self.connection = connection_to_db()
        self.cursor = self.connection.cursor()
        try:
            self.book_title = input("Enter Book Title: ")
            self.query =  '''
                            SELECT * FROM books
                            WHERE title = %s
                            '''
            self.cursor.execute(self.query, (self.book_title,))
            self.columns = self.column_names

            for self.row in self.cursor.fetchall():
                self.row_data = dict(zip(self.columns, self.row))
                print(f"Title: {self.row_data['title']}")
        finally:
            self.cursor.close()
            self.connection.close()
    
    def get_author(self):
        self.connection = connection_to_db()
        self.cursor = self.connection.cursor()
        try:
            self.book_title = input("Enter Book Title: ")
            self.query1 = '''
                            SELECT author_id
                            FROM books
                            WHERE title = %s
                            '''
            self.cursor.execute(self.query1, (self.book_title,))
            self.author_id = self.cursor.fetchone()

            self.query2 = '''
                            SELECT name
                            FROM authors
                            WHERE author_id = %s
                            '''
            self.cursor.execute(self.query2, (self.author_id,))
            self.columns = self.column_names

            for self.row in self.cursor.fetchall():
                self.row_data = dict(zip(self.columns, self.row))
                print(f"Author: {self.row_data['name']}")
        finally:
            self.cursor.close()
            self.connection.close()
    
    def get_genre(self):
        self.connection = connection_to_db()
        self.cursor = self.connection.cursor()
        try:
            self.book_genre = input("Enter Book Title: ")
            self.query = '''
                            SELECT genre
                            FROM books
                            WHERE title = %s
                            '''
            self.cursor.execute(self.query, (self.book_genre,))
            self.columns = self.column_names

            for self.row in self.cursor.fetchall():
                self.row_data = dict(zip(self.columns, self.row))
                print(f"Genre: {self.row_data['genre']}")
        finally:
            self.cursor.close()
            self.connection.close()
    
    def get_publication_date(self):
        self.connection = connection_to_db()
        self.cursor = self.connection.cursor()
        try:
            self.book_title = input("Enter Book Title: ")
            self.query = '''
                            SELECT publication_date
                            FROM books
                            WHERE title %s
                            '''
            self.cursor.execute(self.query, (self.book_title,))
            self.columns = self.cursor.column_names

            for self.row in self.cursor.fetchall():
                self.row_data = dict(zip(self.columns, self.row))
                print(f"Publication Date: {self.row_data['publication_date']}")
        finally:
            self.cursor.close()
            self.connection.close()

    def get_availability(self):
        return self.availability
    
    def switch_availability(self):
        if self.availability == True:
            self.availability = False
        else:
            self.availability = True

# ==================== ***** Functions ***** ====================
# Here down needs fixing
def add_book():
    '''Creates new book and prints confirmation.'''
    clr()
    hr(50)
    try:
        connection = connection_to_db()
        cursor = connection.cursor()

        title = input("Enter Title: ")
        genre = input("Enter Genre: ")
        publication_date = input("Enter Publication Date: ")

        author_name = input("Enter Author: ")
        biography = input("Enter Author Biography: ")

        query1 = '''
                    INSERT INTO authors (name, biography)
                    Values (%s, %s);
                    '''
        cursor.execute(query1, (author_name, biography))
        connection.commit()
        new_author_id = cursor.lastrowid
        

        query2 = '''
                    INSERT INTO books (title, genre, publication_date, author_id)
                    VALUES (%s, %s, %s, %s);
                    '''
        cursor.execute(query2, (title, genre, publication_date, new_author_id))
        connection.commit()

        clr()
        hr(50)
        print(congrats)
        print("The following book has been added:\n")
        print(f"Title: {title}\nAuthor: {author_name}")
        hr(50)
    finally:
        cursor.close()
        connection.close()

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