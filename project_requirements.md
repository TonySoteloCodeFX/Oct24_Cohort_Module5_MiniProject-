<h1>Mini-Project: Library Management System with Database Integration</h1>
<hr>

<h3>Project Requirements</h3>

In this project, you will integrate a MySQL database with Python to develop an advanced Library Management System. This command-line-based application is designed to streamline the management of books and resources within a library. Your mission is to create a robust system that allows users to browse, borrow, return, and explore a collection of books while demonstrating your proficiency in database integration, SQL, and Python.

<h5>Integration with the "Library Management System" Project from Module 4 (OOP):</h5>

For this project, you will build upon the foundation laid in "Module 4: Python Object-Oriented Programming (OOP)." The object-oriented structure and classes you developed in that module will serve as the core framework for the Library Management System. You will leverage the classes such as <b>Book, User, Author, and Genre</b> that you previously designed, extending their capabilities to integrate seamlessly with the MySQL database.

<h5>Enhanced User Interface (UI) and Menu:</h5>

1. Create an improved, user-friendly command-line interface (CLI) for the Library Management System with separate menus for each class of the system.

```
Welcome to the Library Management System with Database Integration!
****
Main Menu:
1. Book Operations
2. User Operations
3. Author Operations
4. Quit
```

<h5>Book Operations:</h5>

```
Book Operations:
1. Add a new book
2. Borrow a book
3. Return a book
4. Search for a book
5. Display all books
```

<h5>User Operations:</h5>

```
User Operations:
1. Add a new user
2. View user details
3. Display all users
```

<h5>Author Operations:</h5>

```
Author Operations:
1. Add a new author
2. View author details
3. Display all authors
```

<h5>Database Integration with MySQL:</h5>

1. Integrate a MySQL database into the Library Management System to store and retrieve data related to books, users, authors, and genres.
<br>

2. Design and create the necessary database tables to represent these entities. You will align these tables with the object-oriented structure from the previous project.
<br>

3. Establish connections between Python and the MySQL database for data manipulation, enhancing the persistence and scalability of your Library Management System.

<h5>Data Definition Language Scripts:</h5>

1. Create the necessary database tables for the Library Management System. For instance:
<br>

2. Books Table:

```
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT,
    isbn VARCHAR(13) NOT NULL,
    publication_date DATE,
    availability BOOLEAN DEFAULT 1,
    FOREIGN KEY (author_id) REFERENCES authors(id),
);
```

<li>Authors Table:</li>

```
CREATE TABLE authors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    biography TEXT
);
```

<li>Users Table:</li>

```
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    library_id VARCHAR(10) NOT NULL UNIQUE
);
```

<li>Borrowed Books Table:</li>

```
CREATE TABLE borrowed_books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    book_id INT,
    borrow_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);
```

💡 **Note:** You can reuse the clean code and functions developed in the "Module 4: Python Object-Oriented Programming (OOP)" project to maintain consistency and reduce redundancy. Emphasize the importance of code reusability and modular design to make it easier to integrate the database functionality into their existing project.

<h5>Submission</h5>

<li>Upon completing the project, submit your code, including all source code files, and the README.md file in your GitHub repository to your instructor or designated platform.</li>

<h5>Project Tips</h5>

1. <b>Reuse Your OOP Project:</b> Take advantage of the object-oriented structure and classes you developed in "Module 4: Python Object-Oriented Programming (OOP)." This will save you time and effort by providing a solid foundation for integrating the database functionality.

<b>NOTE:</b> Ensure that all code in your file is ready to run. This means that if someone opens your file and clicks the run button at the top, all code executes as intended. For example, if there are if statements, print statements, or for loops, they should function correctly and display output in the console as expected. If you have a function, make sure the function is called and runs. If there are classes/objects, make sure they are instantiated and the methods are called.

The goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested.

View Rubric here: <a href="https://codingtemple.notion.site/Module-5-Mini-Project-c7901ed8b58e46c5857ce0bbc32e3c66">Module 5 Mini-Project Rubric</a>