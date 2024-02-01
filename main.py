import requests
from os import getenv
from dotenv import load_dotenv

# Importing models
from models.author import Author
from models.category import Category
from models.book import Book
from models.book_author import BookAuthor
from models.book_category import BookCategory

# Importing repositories
from repositories.author_repository import AuthorRepository
from repositories.category_repository import CategoryRepository
from repositories.book_repository import BookRepository
from repositories.book_author_repository import BookAuthorRepository
from repositories.book_category_repository import BookCategoryRepository

# Importing database related
from db.launcherDB import Launcher

# Load Environment Variables.
load_dotenv()

# Access API key stored in Environment Variables.
# Set your .env file in the root directory with your API key as "GOOGLE_BOOKS_API_KEY=your_key".
API_KEY = getenv("GOOGLE_BOOKS_API_KEY")

# Database default name.
DB_NAME = "database.db"

# The maximum number of books allowed by API.
MAX_NUM_BOOKS = 40

"""Creation of tables if not exists"""
Launcher.create_table_authors(DB_NAME)
Launcher.create_table_categories(DB_NAME)
Launcher.create_table_books(DB_NAME)
Launcher.create_table_book_authors(DB_NAME)
Launcher.create_table_book_categories(DB_NAME)


def search_books(api_key: str, query: str, num_books: int):
    
    if num_books > MAX_NUM_BOOKS:
        return print(f"Maximum number of books allowed is 40 but you have provided {num_books}.")
    
    base_url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        "q": query,
        "key": api_key,
        "maxResults": num_books
    }
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json().get("items", [])
        
        for item in data:
            volume_info = item.get("volumeInfo", {})
            
            """Inserting into books"""            
            name = volume_info.get("title", "N/A")
            publisher = volume_info.get("publisher", "N/A")
            publishedDate = volume_info.get("publishedDate", "N/A")
            description = volume_info.get("description", "N/A")
            pageCount = volume_info.get("pageCount", "N/A")
            
            industry_identifiers = volume_info.get("industryIdentifiers", [])

            ISBN = "N/A"
            for identifier in industry_identifiers:
                if identifier.get("type") == "ISBN_13":
                    ISBN = identifier.get("identifier")
                    break
                elif identifier.get("type") == "ISBN_10":
                    ISBN = identifier.get("identifier")
            
            values = {
                "name": name,
                "publisher": publisher,
                "publishedDate": publishedDate,
                "description": description,
                "ISBN": ISBN,
                "pageCount": pageCount,
            }
            
            bookInformation = BookRepository(DB_NAME).insert_book(Book(**values))
            
            """Inserting into authors"""
            authors = volume_info.get("authors", ["N/A"])
            
            for author in authors:
                author_id = AuthorRepository(DB_NAME).insert_author(Author(author))
                
                """Inserting into book_authors"""
                BookAuthorRepository(DB_NAME).insert_book_author(BookAuthor(author_id, bookInformation.id))
            
            """Inserting into categories"""
            categories = volume_info.get("categories", ["N/A"])
            
            for category in categories:
                category_id = CategoryRepository(DB_NAME).insert_category(Category(category))
            
                """Inserting into book_categories"""
                BookCategoryRepository(DB_NAME).insert_book_category(BookCategory(category_id, bookInformation.id))
            
            
        if "nextPageToken" in response.json():
            params["startIndex"] = response.json()["nextPageToken"]
        else:
            return
        
    except Exception as e:
        print(f"Error fetching books: {e}")

if __name__ == "__main__":
    # List provided by AI.
    books = [
        "1984",
        "A Arte da Guerra",
        "A Culpa é das Estrelas",
        "A Divina Comédia",
        "A História Sem Fim",
        "A Insustentável Leveza do Ser",
        "A Metamorfose",
        "A Montanha Mágica",
        "A Morte de Ivan Ilitch",
        "A Revolução dos Bichos",
        "A Sangue Frio",
        "A Sombra do Vento",
        "A Torre Negra",
        "A Volta ao Mundo em 80 Dias",
        "Alice no País das Maravilhas",
        "Anna Karenina",
        "As Aventuras de Sherlock Holmes",
        "As Crônicas de Nárnia",
        "As Vinhas da Ira",
        "Cem Anos de Solidão",
        "Crime e Castigo",
        "Dom Quixote",
        "Drácula",
        "E Não Sobrou Nenhum",
        "Em Busca do Tempo Perdido",
        "Ensaio sobre a Cegueira",
        "Fahrenheit 451",
        "Frankenstein",
        "Guerra e Paz",
        "Hamlet",
        "Harry Potter e a Pedra Filosofal",
        "Ilíada",
        "Jane Eyre",
        "Laranja Mecânica",
        "Lolita",
        "Macbeth",
        "Maus",
        "Moby Dick",
        "Mrs. Dalloway",
        "O Apanhador no Campo de Centeio",
        "O Cão dos Baskervilles",
        "O Conde de Monte Cristo",
        "O Corcunda de Notre-Dame",
        "O Estrangeiro",
        "O Grande Gatsby",
        "O Hobbit",
        "O Leão, a Feiticeira e o Guarda-Roupa",
        "O Nome da Rosa",
        "O Pequeno Príncipe",
        "O Retrato de Dorian Gray",
        "O Senhor dos Anéis",
        "O Sol é para Todos",
        "Orgulho e Preconceito",
        "Os Irmãos Karamázov",
        "Os Miseráveis",
        "Os Três Mosqueteiros",
        "Paraíso Perdido",
        "Percy Jackson e o Ladrão de Raios",
        "Peter Pan",
        "Romeu e Julieta",
        "Sapiens: Uma Breve História da Humanidade",
        "Siddhartha",
        "Sobre os Ombros de Gigantes",
        "Sobre Ratos e Homens",
        "Sobrevivendo no Inferno",
        "O Sol é para Todos",
        "Terra Sonâmbula",
        "O Triste Fim de Policarpo Quaresma",
        "O Vermelho e o Negro",
        "Viagem ao Centro da Terra",
        "Vidas Secas",
        "Walden",
        "1984",
        "A Revolução dos Bichos",
        "A Hora da Estrela",
        "A Menina que Roubava Livros",
        "A Metamorfose",
        "A Revolução dos Bichos",
        "A Sombra do Vento",
        "A Sangue Frio",
        "A Culpa é das Estrelas",
        "A Insustentável Leveza do Ser",
        "As Veias Abertas da América Latina",
        "Crime e Castigo",
        "Dom Quixote",
        "Ensaio sobre a Cegueira",
        "Fahrenheit 451",
        "Grande Sertão: Veredas",
        "Hamlet",
        "Harry Potter e a Pedra Filosofal",
        "Ilíada",
        "Maus",
        "Memórias Póstumas de Brás Cubas",
        "O Apanhador no Campo de Centeio",
        "O Cortiço",
        "O Estrangeiro",
        "O Grande Gatsby",
        "O Nome da Rosa",
        "O Pequeno Príncipe",
        "O Retrato de Dorian Gray",
        "O Senhor dos Anéis",
        "Os Maias",
        "Paraíso Perdido",
        "Sapiens: Uma Breve História da Humanidade",
        "Vidas Secas"
    ]

    # Making sure that not duplicates.
    books = list(set(books))

    count = 0
    for book in books:
        count += 1
        print(f"{count}/{len(books)} Searching: {book}")
        search_books(API_KEY, book, 40)
    
    
