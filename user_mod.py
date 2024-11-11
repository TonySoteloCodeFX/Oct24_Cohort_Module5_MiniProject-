from helpers import clr, hr
from art import main_user_menu
from sql_connection import connection_to_db

class User:

    def __init__(self, name):
        self.name = name
        self.book_list = []

    def fetch_user_by_name(self):
        self.connection = connection_to_db()

        if self.connection is None:
            print("Failed to connect to database.")
            return
        
        self.cursor = self.connection.cursor()
        try:
            self.name = input("Enter User Name: ")
            self.query = '''
                            SELECT * FROM users 
                            WHERE name = %s
                            '''
            
            self.cursor.execute(self.query, (self.name,))
            for row in self.cursor.fetchall():
                print(row)
        finally:
            self.cursor.close()
            self.connection.close()
            

# ==================== ***** Functions ***** ====================

def add_user():
    '''Creates a new user in user table and assigns an ID'''
    clr()
    hr(50)
    try:
        connection = connection_to_db()
        cursor = connection.cursor()

        name = input("Enter Name: ")
        query = '''
                INSERT INTO users (name)
                VALUES (%s);
                '''
        cursor.execute(query, (name,))
        connection.commit()
        new_user_id = cursor.lastrowid
        clr()
        hr(50)
        print("The following user has been created.\n")
        print(f"Library ID: {new_user_id}\nUser: {name}")

    except ValueError:
        clr()
        hr(50)
        print("Invalid Input. Try again.")

    finally:
        cursor.close()
        connection.close()

def display_all_users():
    clr()
    hr(50)
    try:
        connection = connection_to_db()
        cursor = connection.cursor()

        query = '''SELECT * FROM users'''
        cursor.execute(query)
        columns = cursor.column_names

        print(f"All Users:\n")

        for row in cursor.fetchall():
            hr(50)
            row_data = dict(zip(columns, row))

            print(f"ID: {row_data['id']}\nName: {row_data['name']}")
        hr(50)
    finally:
        cursor.close()
        connection.close()

def view_user_details():
    clr()
    hr(50)
    try:
        connection = connection_to_db()
        cursor = connection.cursor()

        print("Who's details would you like to see?\n")
        user_name = input("Enter Name: ")
        query = '''
                    SELECT * FROM users
                    WHERE name = %s
                '''
        cursor.execute(query, (user_name,))
        columns = cursor.column_names

        clr()
        hr(50)
        print(f"User Details:\n")

        for row in cursor.fetchall():
            hr(50)
            row_data = dict(zip(columns, row))

            print(f"ID: {row_data['id']}\nName: {row_data['name']}\nBook Borrowed: {row_data['borrowed_books']}")
        hr(50)
    finally:
        cursor.close()
        connection.close()

def user_menu():
    clr()
    hr(50)
    user_ops_menu = True
    while user_ops_menu:
        try:
            print(main_user_menu)
            print('''
    User Menu:
            1. Add a new user
            2. View user details
            3. Display all users
            4. Return to main menu
                  ''')
            user_operation = int(input("Enter Number: "))

            if user_operation == 1:
                add_user()
            elif user_operation == 2:
                view_user_details()
            elif user_operation == 3:
                display_all_users()
            elif user_operation == 4:
                clr()
                hr(50)
                user_ops_menu = False
            else:
                clr()
                hr(50)
                print(f"{user_operation} is not an option. Try again.")
        except ValueError:
            clr()
            hr(50)
            print("Input must be a number between 1-4")