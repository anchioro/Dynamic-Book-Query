from models.book_category import BookCategory
from db.query import Query

class BookCategoryRepository:
    """Repository for book categories.
    
    Attributes:
        db_name(str): Name of the database.
    """
    
    def __init__(self, db_name: str):
        self.query = Query(db_name)
        
    def insert_book_category(self, book_category: BookCategory):
        """Insert a book category into the database.
        
        Args:
            book_category(BookCategory): Book category to insert.
        """

        query = "INSERT INTO book_categories(category_id, book_id) VALUES(?, ?)"
        values = (book_category.category_id, book_category.book_id)
        
        try:
            self.query.execute_query(query, *values)
            book_category.id = self.query.get_last_id_inserted("book_categories")
            return book_category
        except Exception as e:
            print(f"Error inserting book categories: {e}")
            return None