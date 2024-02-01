from models.author import Author
from db.query import Query

class AuthorRepository:
    """Repository for author.
    
    Attributes:
        db_name(str): Name of the database.
    """
    
    def __init__(self, db_name: str):
        self.query = Query(db_name)

    def insert_author(self, author: Author):
        """Insert a new author into the database.
        
        Args:
            author(Author): The author to insert.
        """
        
        query = "INSERT INTO authors(name) VALUES(?)"
        
        try:
            self.query.execute_query(query, author.name)
            author.id = self.query.get_last_id_inserted("authors")
            return author.id
        except Exception as e:
            print(f"Error inserting authors: {e}")
            return None