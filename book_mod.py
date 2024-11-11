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
    clr()
    hr(50)
    try:
        connection = connection_to_db()
        cursor = connection.cursor()
        print("Books in Library:\n")

        query = '''SELECT * FROM books'''
        cursor.execute(query)
        column = cursor.column_names
        book = cursor.fetchall()

        for row in book:
            hr(50)
            row_data = dict(zip(column, row))
            print(f"ID: {row_data['id']}\nTitle: {row_data['title']}\nGenre: {row_data['genre']}")
        hr(50)
    finally:
        cursor.close()
        connection.close()

def search_book():
    clr()
    hr(50)
    try:
        connection = connection_to_db()
        cursor = connection.cursor()

        print("\nWhich book title would you like to search for?")
        lookup_title = input("Enter Title: ")

        query1 = '''
                    SELECT * FROM books
                    WHERE title = %s;
                '''
        cursor.execute(query1, (lookup_title,))
        book_results = cursor.fetchall()

        if not book_results:
            print("Title not found.")
            return
        clr()
        hr(50)
        print("Book Details:\n")

        for row in book_results:
            columns = cursor.column_names
            row_data = dict(zip(columns, row))

            fetch_availability = row_data['availability']
            if fetch_availability == 1:
                availability = "Book is available."
            else:
                availability = "Book is not available."

            search_author_id = row_data['author_id']

            query2 = '''
                        SELECT name
                        FROM authors
                        WHERE id = %s;
                    '''
            cursor.execute(query2, (search_author_id,))
            author_id = cursor.fetchone()
            author_name = author_id[0]

            print(f'''ID: {row_data['id']}\nTitle: {row_data['title']}\nAuthor: {author_name}\nGenre: {row_data['genre']}\nPublication Date: {row_data['publication_date']}\nAvailability: {availability}''')
        hr(50)

    finally:
        cursor.close()
        connection.close()

def borrow_book():
    clr()
    hr(50)
    try:
        connection = connection_to_db()
        cursor = connection.cursor()

        user_name = input("Enter your name: ")
        query1 = '''
                    SELECT * FROM users
                    WHERE name = %s;
                '''
        cursor.execute(query1, (user_name,))
        columns = cursor.column_names
        
        for row in cursor.fetchall():      
            row_data = dict(zip(columns, row))
            status = row_data['borrowed_status']
            book_borrowed = row_data['borrowed_books']
            user_id = row_data['id']

            if status != 1:
                clr()
                hr(50)
                print(f"Sorry {user_name},\nYou can borrow a book once {book_borrowed}, is returned.")
                hr(50)
                return
        clr()
        hr(50)
        print(f"Hi {user_name},\nWhat book would you like to borrow?\n")
        book_to_borrow = input("Enter Book Title: ")

        query2 = '''
                    SELECT *
                    FROM books
                    WHERE title = %s;
                '''
        cursor.execute(query2, (book_to_borrow,))
        columns2 = cursor.column_names

        for row in cursor.fetchall():
            row_data2 = dict(zip(columns2, row))
            book_title = row_data2['title']
            book_id = row_data2['id']

            if not book_title:
                clr()
                hr(50)
                print(f"Sorry {user_name},\nWe don't seem to have this book.")
                hr(50)
                return
            elif row_data2['availability'] != 1:
                clr()
                hr(50)
                print(f"Sorry {user_name},\n{book_title}, is not currently available.")
                hr(50)
                return
            
        query3 = '''
                    UPDATE books
                    SET availability = FALSE
                    WHERE title = %s;
                '''
        cursor.execute(query3, (book_to_borrow,))
        connection.commit()

        query4 = '''
                    UPDATE users 
                    SET borrowed_books = %s, borrowed_status = FALSE
                    WHERE name = %s;
                    '''
        cursor.execute(query4, (book_to_borrow, user_name))
        connection.commit()

        query5 = '''
                    INSERT INTO books_borrowed (book_id, user_id)
                    VALUES (%s, %s);
                '''
        cursor.execute(query5, (book_id, user_id))
        connection.commit()

        clr()
        hr(50)
        print(congrats)
        print(f"Congratulations {user_name}!\nYou have just borrowed {book_to_borrow}!\nPlease return it before borrowing another book.\nThank you!")
        hr(50)
    finally:
        cursor.close()
        connection.close()

def return_book():
    clr()
    hr(50)
    try:
        connection = connection_to_db()
        cursor = connection.cursor()

        user_name = input("Enter your name: ")
        query1 = '''
                    SELECT * FROM users
                    WHERE name = %s;
                '''
        cursor.execute(query1, (user_name,))
        columns = cursor.column_names

        for row in cursor.fetchall():      
            row_data = dict(zip(columns, row))
            status = row_data['borrowed_status']
            book_borrowed = row_data['borrowed_books']
            user_id = row_data['id']

            if status == 1:
                clr()
                hr(50)
                print(f"Sorry {user_name},\nYou don't have any books to return at the moment.")
                hr(50)
                return
            
        query2 =  '''
                    UPDATE users
                    SET borrowed_status = TRUE, borrowed_books = NULL
                    WHERE id = %s;
                '''
        cursor.execute(query2, (user_id,))
        connection.commit()

        query3 = '''
                    UPDATE books
                    SET availability = TRUE
                    WHERE title = %s;
                '''
        cursor.execute(query3, (book_borrowed,))
        connection.commit()

        query4 = '''
                    DELETE FROM books_borrowed
                    WHERE user_id = %s;
                '''
        clr()
        hr(50)
        print(congrats)
        print(f"Hi {user_name}!\nThank you for returning {book_borrowed}.")
        print("You're now able to borrow another book. Thank you.")
        hr(50)

        cursor.execute(query4, (user_id,))
        connection.commit()

    finally:
        cursor.close()
        connection.close()


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