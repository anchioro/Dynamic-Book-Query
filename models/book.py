"""Book model"""

class Book:
    """Class representing a book.
    
    Attributes:
        id (int): The id of the book.
        name (str): The name of the book.
        publisher (str): The publisher of the book.
        publishedDate (str): The published date of the book.
        description (str): The description of the book.
        ISBN (str): The ISBN of the book.
        pageCount (int): The number of pages in the book.
    """

    def __init__(self, name: str, publisher: str, publishedDate: str,
                 description: str, ISBN: str, pageCount: int, id: int = None):
        
        self.name = name
        self.publisher = publisher
        self.publishedDate = publishedDate
        self.description = description
        self.ISBN = ISBN
        self.pageCount = pageCount
        self.id = id

    def __str__(self) -> str:
        return f"ID: {self.id}\n" \
               f"Name: {self.name}\n" \
               f"Publisher: {self.publisher}\n" \
               f"Published Date: {self.publishedDate}\n" \
               f"Description: {self.description}\n" \
               f"ISBN: {self.ISBN}\n" \
               f"Page Count: {self.pageCount}"

    def __repr__(self) -> str:
        return f"Book(id={self.id}, name={self.name}, publisher={self.publisher}, " \
               f"publishedDate={self.publishedDate}, description={self.description}, " \
               f"ISBN={self.ISBN}, pageCount={self.pageCount}"
