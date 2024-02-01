from models.book_author import BookAuthor
from db.query import Query

class BookAuthorRepository:
    """Repository for book authors.
    
    Attributes:
        db_name(str): Name of the database.
    """
    
    def __init__(self, db_name: str):
        self.query = Query(db_name)
        
    def insert_book_author(self, book_author: BookAuthor):
        """Insert a book author into the database.
        
        Args:
            book_author(BookAuthor): Book author to insert.
        """

        query = "INSERT INTO book_authors(author_id, book_id) VALUES(?, ?)"
        values = (book_author.author_id, book_author.book_id)
        
        try:
            self.query.execute_query(query, *values)
            book_author.id = self.query.get_last_id_inserted("book_authors")
            return book_author
        except Exception as e:
            print(f"Error inserting book authors: {e}")
            return None