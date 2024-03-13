# Library Database Management

This Python script is designed to manage a library database using SQLite. It provides functionality to create a table for storing book information, insert sample book data into the table, perform various operations such as retrieving all books, calculating the average number of pages, finding the book with the maximum number of pages, and more.

## Features

- **Creating Table**: The script creates a table named `books` with columns for book name, page number, cover type, and category.
  
- **Inserting Books**: Sample book data is provided in the `get_books()` function. The script inserts this data into the `books` table using the `insert_books()` function.

- **Selecting Books**: The `select_books()` function retrieves all books from the `books` table and returns them as a list of tuples.

- **Calculating Average Page Number**: The `get_avg_page_number()` function calculates the average number of pages across all books in the library.

- **Finding Biggest Book**: The `get_biggest_book()` function finds the book with the maximum number of pages in the library.

## Usage

To use this script:

1. Make sure you have Python installed on your system.

2. Install the required SQLite module if not already installed:
   ```
   pip install sqlite3
   ```

3. Run the script `main.py`. This will execute the main function, which performs various operations on the library database.

4. View the output to see the results of the operations, including the number of affected rows during insertion, the list of all books, the average number of pages, and the details of the biggest book.

## Notes

- The script assumes that an SQLite database file named `library.db` exists in the current directory. If not, it will be created automatically.
  
- Modify the `get_books()` function to provide your own book data or integrate it with an external data source.
  
- Customize the database schema or modify the SQL queries to suit your specific requirements.