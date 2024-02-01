"""Author model"""

class Author:
    """Class representing the author.
    
    Attributes:
        id (int): The id of the author.
        name (str): The name of the author.
    """
    
    def __init__(self, name: str, id: int = None):
        self.name = name
        self.id = id

    def __str__(self) -> str:
        return f"ID: {self.id}" \
               f"Name: {self.name}"
               
    def __repr__(self) -> str:
        return f"ID: {self.id}" \
               f"Name: {self.name}"