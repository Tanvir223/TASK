import sqlite3

def create_table():
    # Connect to SQLite database (or create a new one if it doesn't exist)
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    # Create a table to store book information
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            year INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def add_book(title, author, year):
    # Add a new book to the database
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO books (title, author, year)
        VALUES (?, ?, ?)
    ''', (title, author, year))
    conn.commit()
    print(f'Book "{title}" added successfully.')
    conn.close()

def retrieve_books():
    # Retrieve all books from the database
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    
    conn.close()

    if not books:
        print('No books found.')
    else:
        for book in books:
            print(f'ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}')

def update_book(book_id, title, author, year):
    # Update book information
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE books
        SET title=?, author=?, year=?
        WHERE id=?
    ''', (title, author, year, book_id))
    conn.commit()
    print(f'Book with ID {book_id} updated successfully.')
    conn.close()

def delete_book(book_id):
    # Delete a book from the database
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM books WHERE id=?', (book_id,))
    conn.commit()
    print(f'Book with ID {book_id} deleted successfully.')
    conn.close()


create_table()

add_book('The Great Gatsby', 'F. Scott Fitzgerald', 1925)
add_book('To Kill a Mockingbird', 'Harper Lee', 1960)
retrieve_books()

# update_book(1, 'The Great Gatsby (Updated)', 'F. Scott Fitzgerald', 1925)
# delete_book(2)

# retrieve_books()

