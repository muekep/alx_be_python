class Book:
    
    # Represents a book with a title, author, and availability status.
    
    def __init__(self, title: str, author: str):
    
        #Initializes a new Book instance.

        #Args:
            #title (str): The title of the book.
            #author (str): The author of the book.
      
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute, defaults to False (available)

    def __str__(self):
        
        # Returns a string representation of the Book object for easy printing.
       
        status = "Checked Out" if self._is_checked_out else "Available"
        return f"'{self.title}' by {self.author} ({status})"

    def get_status(self) -> bool:
        """
        Returns the current checked out status of the book.
        True if checked out, False if available.
        """
        return self._is_checked_out

    def _set_checked_out_status(self, status: bool):
        """
        Internal method to set the checked out status.
        Used by the Library class.
        """
        self._is_checked_out = status


class Library:
    """
    Manages a collection of books, allowing adding, checking out,
    returning, and listing available books.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list of books.
        """
        self._books = []  # Private list to store Book objects

    def add_book(self, book: Book):
        """
        Adds a Book instance to the library's collection.

        Args:
            book (Book): The Book object to add.
        """
        # Optional: Add logic to prevent adding duplicate books by ISBN if that were an attribute
        self._books.append(book)
        print(f"Added '{book.title}' by {book.author} to the library.")

    def check_out_book(self, title: str) -> bool:
        """
        Attempts to check out a book by its title.

        Args:
            title (str): The title of the book to check out.

        Returns:
            bool: True if the book was successfully checked out, False otherwise.
        """
        # Iterate through books to find the one with the matching title
        # For simplicity, we'll operate on the first match found.
        # Consider a unique identifier like ISBN for robust lookup in a real system.
        found_book = None
        for book in self._books:
            if book.title.lower() == title.lower(): # Case-insensitive search
                found_book = book
                break

        if found_book:
            if not found_book.get_status(): # If _is_checked_out is False (i.e., available)
                found_book._set_checked_out_status(True)
                print(f"Successfully checked out '{found_book.title}'.")
                return True
            else:
                print(f"'{found_book.title}' is already checked out.")
                return False
        else:
            print(f"Book with title '{title}' not found in the library.")
            return False

    def return_book(self) -> bool:
        """
        Attempts to return a book by its title.

        Args:
            title (str): The title of the book to return.

        Returns:
            bool: True if the book was successfully returned, False otherwise.
        """
        found_book = None
        for book in self._books:
            if book.title.lower() == title.lower(): # Case-insensitive search
                found_book = book
                break

        if found_book:
            if found_book.get_status(): # If _is_checked_out is True (i.e., checked out)
                found_book._set_checked_out_status(False)
                print(f"Successfully returned '{found_book.title}'.")
                return True
            else:
                print(f"'{found_book.title}' is already available (not checked out).")
                return False
        else:
            print(f"Book with title '{title}' not found in the library.")
            return False

    def list_available_books(self):
        """
        Prints a list of all books currently available in the library.
        """
        available_books = [book for book in self._books if not book.get_status()]

        if not available_books:
            print("No books are currently available in the library.")
        else:
            print("\n--- Available Books ---")
            for i, book in enumerate(available_books, 1):
                print(f"{i}. {book.title} by {book.author}")
            print("-----------------------")
