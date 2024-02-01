from models.category import Category
from db.query import Query

class CategoryRepository:
    """Repository for category.
    
    Attributes:
        db_name(str): Name of the database.
    """
    
    def __init__(self, db_name: str):
        self.query = Query(db_name)

    def insert_category(self, category: Category):
        """Insert a new category into the database.
        
        Args:
            category(Category): The category to insert.
        Returns:
            if insert succeeds returns the category ID.
        """
        
        query = "INSERT INTO categories(name) VALUES(?)"
        
        try:
            self.query.execute_query(query, category.name)
            category.id = self.query.get_last_id_inserted("categories")
            return category.id
        except Exception as e:
            print(f"Error inserting category: {e}")
            return None