import sqlite3

class Launcher():
    """Class responsible to launch the data base."""
    
    def create_table_authors(db_name: str):
        """Creates a table of authors.
        
        Args:
            db_name: Database name.
        """
        
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS authors (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL UNIQUE
                           );
                       """)
        
        connection.commit()
        cursor.close()
        
    def create_table_categories(db_name: str):
        """Creates the table of categories.
        
        Args:
            db_name(str): Database name.
        """
        
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS categories(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL UNIQUE
                           );
                       """)

    def create_table_books(db_name: str):
        """Creates the table of books.
        
        Args:
            db_name(str): database name.
        """

        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()

        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS books(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            publisher TEXT NOT NULL,
                            publishedDate TEXT NOT NULL,
                            description TEXT,
                            ISBN TEXT NOT NULL UNIQUE,
                            pageCount INTEGER NOT NULL
                            );
                        """)
        
        connection.commit()
        cursor.close()

    def create_table_book_authors(db_name: str):
        """Creates the table of book authors.
        
        Args:
            db_name: The name of the database.
        """
        
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS book_authors (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           author_id INTEGER,
                           book_id INTEGER,
                           UNIQUE(author_id, book_id),
                           FOREIGN KEY (author_id) REFERENCES authors(id),
                           FOREIGN KEY (book_id) REFERENCES books(id)
                           );
                       """)
        
        connection.commit()
        cursor.close()
        
    def create_table_book_categories(db_name: str):
        """Creates the table of book categories.
        
        Args:
            db_name(str): The name of the database.
        """
        
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS book_categories(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           category_id INTEGER UNIQUE,
                           book_id INTEGER UNIQUE,
                           FOREIGN KEY (category_id) REFERENCES categories(id),
                           FOREIGN KEY (book_id) REFERENCES books(id)
                           );
                       """)
        
        connection.commit()
        cursor.close()
