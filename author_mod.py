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
# From here down needs fixing 
def add_author():
    clr()
    hr(50)
    try:
        name = input("Enter Author's Name: ")
        biography = input("Enter Biography: ")
        new_author = Author(name, biography)
        clr()
        hr(50)
        print("The following author has been added.\n")
        print(f"Name: {new_author.name}\nBiography: {new_author.biography}")
    except ValueError:
        print("Invalid Input. Try again.")

def display_authors():
    Author.display_all_authors()

def view_author_details():
    clr()
    hr(50)
    author_name = input("Enter Author's Name: ")

    author_to_view = None
    for author in Author.authors:
        if author.get_author_name() == author_name:
            author_to_view = author
            break

    if author_to_view:
        clr()
        hr(50)
        print(f"Name: {author_to_view.get_author_name()}")
        print(f"Biography: {author_to_view.get_biography()}")
        hr(50)
    else:
        print(f"Author: {author_name} not found.")

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
                pass
            elif author_operation == 2:
                pass
            elif author_operation == 3:
                pass
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