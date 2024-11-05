from helpers import clr, hr
from art import main_user_menu
from sql_connection import connection_to_db

connection = connection_to_db()
cursor = connection.cursor()

class User:
    users = []
    user_id = 0

    def __init__(self, name):
        self.name = name
        self.book_list = []
        User.user_id += 1
        self.user_id = User.user_id
        User.users.append(self)

    def get_user_name(self):
        return self.name
    
    def get_user_id(self):
        return self.user_id

    @classmethod
    def display_all_users(cls):
        clr()
        hr(50)
        print("All Users")
        for user in cls.users:
            hr(50)
            print(f"Library ID: {user.get_user_id()}")
            print(f"User Name: {user.get_user_name()}")

# ==================== ***** Functions ***** ====================
# def sql_add_user():
#     try:
#         full_name = input("Enter Full Name: ")

def add_user():
    clr()
    hr(50)
    try:
        name = input("Enter Name: ")
        new_user = User(name)
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
        print(f"Library ID: {new_user.user_id}\nUser: {new_user.name}")

    except ValueError:
        print("Invalid Input. Try again.")

    finally:
        cursor.close()
        connection.close()

def display_users():
    User.display_all_users()

def view_details():
    clr()
    hr(50)
    view_user = input("Enter Name: ")

    user_to_view = None
    for user in User.users:
        if user.get_user_name() == view_user:
            user_to_view = user
            break
    if user_to_view:
        clr()
        hr(50)
        print(f"User ID: {user_to_view.get_user_id()}")
        print(f"User Name: {user_to_view.get_user_name()}")
        hr(50)
        if user_to_view.book_list:
            print("Books Borrowed: ")
            for book in user_to_view.book_list:
                print(f"Title: {book.get_title()}\n")
        else:
            print("No books borrowed.")
        hr(50)
    else:
        print(f"User: {view_user} not found.")

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
                view_details()
            elif user_operation == 3:
                display_users()
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