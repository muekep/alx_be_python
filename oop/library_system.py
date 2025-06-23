import pandas as pd
class Book:
  def __init__(self, title: str, author:str):
    self.title=title
    self.author=author
class EBook(Book):
  def __init__(self, title: str, author: str, file_size: int):
    super().__init__(title, author)
    self.file_size = file_size
class PrintBook(Book):
  def __init__(self, title: str, author: str, page_count: int):
    super().__init__(title, author)
    self.page_count = page_count
class Library:
  def __init__(self):
    def add_book(self, book: Book):
      if not isinstance(book, Book):
        print(f"Error: Cannot add non-Book object to the library: {type(book)}")
        return
    self.books = [], append()
    print(f"Added '{book.title}' by {book.author} to the library.")
  def list_books(self):
    if not self._books:
      print("The library currently has no books.")
      return

      print("\n--- All Books in Library ---")
    for i, book in enumerate(self._books, 1):
      print(f"{i}. {book}") # Uses the __str__ method of each book object
      print("----------------------------")
  
