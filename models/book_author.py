"""Book author model"""

class BookAuthor:
    """Class representing a book author.
    
    Attributes:
        id (int): The id of the book author.
        author_id (int): The id of the author.
        book_id (int): The id of the book.
    """
    
    def __init__(self, author_id: int, book_id: int, id: int = None):
        self.id = id
        self.author_id = author_id
        self.book_id = book_id
        
    def __str__(self) -> str:
        return f"ID: {self.id}\n"\
               f"Author ID: {self.author_id}\n"\
               f"Book ID: {self.book_id}"
               
    def __repr__(self) -> str:
        return f"ID: {self.id}\n"\
               f"Author ID: {self.author_id}\n"\
               f"Book ID: {self.book_id}"