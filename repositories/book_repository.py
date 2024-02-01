from models.book import Book
from db.query import Query

class BookRepository:
    """Repository for book.
    
    Attributes:
        db_name(str): Name of the database.
    """
    
    def __init__(self, db_name: str):
        self.query = Query(db_name)
        
    def insert_book(self, book: Book):
        """Insert a book into the database.
        
        Args:
            book(Book): Book to be inserted.
        """
        
        query = "INSERT INTO books(name, publisher, publishedDate, description, ISBN, pageCount) VALUES(?, ?, ?, ?, ?, ?)"
        
        values = (book.name, book.publisher, book.publishedDate, book.description, book.ISBN, book.pageCount)
        
        
        try:
            self.query.execute_query(query, *values)
            book.id = self.query.get_last_id_inserted("books")
            return book
        except Exception as e:
            print(f"Error inserting book: {e}")
            return None
