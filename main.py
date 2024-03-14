import sqlite3


def get_books():
    books = [
        ("The Great Gatsby", 180, "Hardcover", "Fiction"),
        ("To Kill a Mockingbird", 281, "Paperback", "Fiction"),
        ("1984", 328, "Hardcover", "Science Fiction"),
        ("Pride and Prejudice", 279, "Paperback", "Romance"),
        ("The Catcher in the Rye", 224, "Hardcover", "Fiction"),
        ("The Hobbit", 310, "Paperback", "Fantasy"),
        ("Harry Potter and the Sorcerer's Stone", 320, "Hardcover", "Fantasy"),
        ("The Da Vinci Code", 454, "Paperback", "Mystery"),
        ("The Lord of the Rings", 1178, "Hardcover", "Fantasy"),
        ("The Hitchhiker's Guide to the Galaxy", 216, "Paperback", "Science Fiction")
    ]

    return books


def create_table(cursor):
    cursor.execute("""
            CREATE TABLE books (
            book_name text,
            page_number integer,
            cover_type text,
            category text)""")


def insert_books(conn, cursor, books):
    cursor.executemany("INSERT INTO books VALUES(?, ?, ?, ?)", books)
    conn.commit()
    return cursor.rowcount


def select_books(cursor):
    res = cursor.execute("SELECT * FROM books")

    return res.fetchall()


def delete_books(cursor):
    res = cursor.execute("DELETE FROM books")

    return res.rowcount


def get_avg_page_number(cursor):
    res = cursor.execute("SELECT AVG(page_number) FROM books")

    return res.fetchone()[0]


def get_biggest_book(cursor):
    res = cursor.execute("SELECT book_name, MAX(page_number) FROM books")

    return res.fetchone()


def main():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    create_table(cursor)
    res = insert_books(conn, cursor, get_books())
    print(f"Affected rows {res}.")
    print(select_books(cursor))
    print(f"Average number of pages: {get_avg_page_number(cursor)}")
    book_name, page_number = get_biggest_book(cursor)
    print(f"Biggest book is '{book_name}' with {page_number} pages.")
    conn.close()


if __name__ == '__main__':
    main()

