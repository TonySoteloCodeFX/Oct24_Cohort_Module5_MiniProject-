CREATE DATABASE library_management_System;
USE library_management_System;

CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE books (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    genre VARCHAR(50) NOT NULL,
    publication_date DATE,
    availability BOOLEAN DEFAULT TRUE
);

CREATE TABLE authors (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    biography VARCHAR(300)
);

CREATE TABLE books_borrowed (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY
);

ALTER TABLE books
ADD author_id INT,
ADD FOREIGN KEY (author_id) REFERENCES authors(id);

ALTER TABLE users
ADD COLUMN borrowed_status BOOLEAN DEFAULT TRUE;

SELECT * FROM books;
SELECT * FROM authors;
SELECT * FROM users;
SELECT * FROM books_borrowed;

UPDATE users 
SET borrowed_books = None
WHERE id  = 8;


