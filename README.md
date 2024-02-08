# Python Book Search Application

The Python Book Search Application allows users to search for books using the Google Books API. It dynamically populates the database with book information retrieved from the API based on user queries.

## Installation

Before running the application, make sure you have Python and pip installed on your system.

### 1. Install Required Packages

Use [pip](https://pip.pypa.io/en/stable/) to install the necessary dependencies listed in `requirements.txt` file.

> bash
```bash
pip install -r requirements.txt
```

### 2. Set up Google Books API Key

To access the Google Books API, you need to obtain an API key and set it up using environment variables.

#### Setting up the .env file

In order to securely store your API key, you'll need to create a `.env` file in the root directory of your project. Follow these steps:

1. Create a file named .env in the root directory.
2. Add your [Google Books API](https://developers.google.com/books/docs/v1/using) key to the .env file in the following format:


> .env
```.env
GOOGLE_BOOKS_API_KEY=your_api_key_here
```
Replace `your_api_key_here` with the actual API key you obtained from the Google API.

## Usage

The primary function for interacting with the application is `search_book()`.

### Parameters

1. `api_key:`  Your Google Books API key.
2. `query:` The search query for finding books.
3. `num_books:` The maximum number of books to retrieve.

### Example

>main.py
```python
def search_books(api_key: str, query: str, num_books: int)
    ...

if __name__ == "__main__":
    search_books(API_KEY, "python", 40)
```
Running the script initiates a search for books related to "python" using the provided API key and retrieves a maximum of 40 books. The database is created automatically to store the retrieved information.
