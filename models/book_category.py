"""Book category model"""

class BookCategory:
    """Class representing a book category.
    
    Attributes:
        id (int): The id of the book category.
        category_id (int): The id of the category.
        book_id (int): The id of the book.
    """
    
    def __init__(self, category_id: int, book_id: int, id: int = None):
        self.id = id
        self.category_id = category_id
        self.book_id = book_id
        
    def __str__(self) -> str:
        return f"ID: {self.id}\n"\
               f"Author ID: {self.category_id}\n"\
               f"Book ID: {self.book_id}"
               
    def __repr__(self) -> str:
        return f"ID: {self.id}\n"\
               f"Author ID: {self.category_id}\n"\
               f"Book ID: {self.book_id}"
               