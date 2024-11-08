# Installing and import MYSQL - pip install-connector-python

import mysql.connector
from mysql.connector import Error


def connection_to_db():
    db_name = 'library_management_System'
    user = 'root'
    password = "Isaiah3117"
    host = '127.0.0.1'

    try:
        # connecting to database 
        connection = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        if connection.is_connected():
            print("Connected to Library Management System successfully.")
            return connection
    
    except Error as e:
        # handle any connection errors 
        print(f"Error: {e}")
        return None
        