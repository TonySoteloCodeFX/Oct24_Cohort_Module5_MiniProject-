from helpers import clr, hr
from art import main_author_menu
from sql_connection import connection_to_db

class Author:

    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

    def fetch_author_by_name(self):
        self.connection = connection_to_db()

        if self.connection is None:
            print("Failed to connect to database.")
            return
        
        self.cursor = self.connection.cursor()
        try:
            self.name = input("Enter Author Name: ")
            self.query = '''
                            SELECT * From authors
                            WHERE name = %s
                            '''
            self.cursor.execute(self.query, (self.name,))
            for row in self.cursor.fetchall():
                print(row)
        finally:
            self.cursor.close()
            self.connection.close()

    def fetch_biography(self):
        self.connection = connection_to_db()

        if self.connection is None:
            print("Failed to connect to database.")
            return
        
        self.cursor = self.connection.cursor()
        try:
            self.name = input("Enter Author Name: ")
            self.query = '''
                            SELECT biography FROM authors
                            WHERE name = %s
                            '''
            self.cursor.execute(self.query, (self.name,))
            for row in self.cursor.fetchall():
                print(row)
        finally:
            self.cursor.close()
            self.connection.close()

# ==================== ***** Functions ***** ====================

def add_author():
    clr()
    hr(50)
    try:
        connection = connection_to_db()
        cursor = connection.cursor()

        name = input("Enter Author's Name: ")
        biography = input("Enter Biography: ")

        query = '''
                    INSERT INTO authors (
                    name, 
                    biography)
                    Values (%s, %s);
                    '''
        cursor.execute(query, (name, biography))
        connection.commit()
        new_author_id = cursor.lastrowid

        clr()
        hr(50)
        print("The following author has been added:\n")
        print(f"Author ID: {new_author_id}\nName: {name}")

    except ValueError:
        clr()
        hr(50)
        print("Invalid Input. Try again.")

    finally:
        cursor.close()
        connection.close()

def view_author_details():
    clr()
    hr(50)
    try:
        connection = connection_to_db()
        cursor = connection.cursor()
        name = input("Enter Author Name: ")

        query = '''
                SELECT * FROM authors
                WHERE name = %s
                '''
        cursor.execute(query, (name,))
        columns = cursor.column_names

        print("Author Details:")

        for row in cursor.fetchall():
            hr(50)
            row_data = dict(zip(columns, row))
            print(f"ID: {row_data['id']}\nName: {row_data['name']}\nBio: {row_data['biography']}")
        hr(50)

    finally:
        cursor.close()
        connection.close()
# From here down needs fixing 
def display_authors():
    clr()
    hr(50)
    try:
        connection = connection_to_db()
        cursor = connection.cursor()

        query = '''SELECT * FROM authors'''
        cursor.execute(query)
        columns = cursor.column_names

        print("All Authors:")

        for row in cursor.fetchall():
            hr(50)
            row_data = dict(zip(columns, row))
            print(f"ID: {row_data['id']}\nName: {row_data['name']}")
            hr(50)

    finally:
        cursor.close()
        connection.close()


def author_menu():
    clr()
    hr(50)
    author_ops_menu = True
    while author_ops_menu:
        try:
            print(main_author_menu)
            print('''
  Author Menu:
            1. Add a new author
            2. View author details
            3. Display all authors
            4. Return to main menu
                  ''')
            author_operation = int(input("Enter Number: "))

            if author_operation == 1:
                add_author()
            elif author_operation == 2:
                view_author_details()
            elif author_operation == 3:
                display_authors()
            elif author_operation == 4:
                clr()
                hr(50)
                author_ops_menu = False
            else:
                clr()
                hr(50)
                print(f"{author_operation} is not an option. Try again.")
        except ValueError:
            clr()
            hr(50)
            print("Input must be a number between 1-4.")