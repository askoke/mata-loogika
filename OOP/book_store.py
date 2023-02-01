"""Book store."""


class Book:
    """Represent book model."""

    def __init__(self, title: str, author: str, price: float, rating: float):
        """
        Class constructor. Each book has title, author and price.

        :param title: book's title
        :param author: book's author
        :param price: book's price
        """
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating

    def __repr__(self):
        """Return book's title and author."""
        return f"{self.title} by {self.author}"


class Store:
    """Represent book store model."""

    def __init__(self, name: str, rating: float):
        """
        Class constructor.

        Each book store has name.
        There also should be an overview of all books present in store

        :param name: book store name
        """
        self.name = name
        self.rating = rating
        self.books_on_sale = []

    def can_add_book(self, book: Book) -> bool:
        """
        Check if book can be added.

        It is possible to add book to book store if:
        1. The book with the same author and title is not yet present in this book store
        2. book's own rating is >= than store's rating
        :return: bool
        """
        if book.rating >= self.rating:
            if len(self.books_on_sale) == 0:
                return True
            else:
                for store_book in self.books_on_sale:
                    if store_book.title == book.title and store_book.author == book.author:
                        return False
                    else:
                        return True
        else:
            return False

    def add_book(self, book: Book):
        """
        Add new book to book store if possible.

        :param book: Book
        Function does not return anything
        """
        if self.can_add_book(book) is True:
            self.books_on_sale.append(book)

    def can_remove_book(self, book: Book) -> bool:
        """
        Check if book can be removed from store.

        Book can be successfully removed if it is actually present in store

        :return: bool
        """
        if book in self.books_on_sale:
            return True
        else:
            return False

    def remove_book(self, book: Book):
        """
        Remove book from store if possible.

        Function does not return anything
        """
        if self.can_remove_book(book) is True:
            self.books_on_sale.remove(book)

    def get_all_books(self) -> list:
        """
        Return a list of all books in current store.

        :return: list of Book objects
        """
        return self.books_on_sale

    def get_books_by_price(self) -> list:
        """
        Return a list of books ordered by price (from cheapest).

        :return: list of Book objects
        """
        books_by_price = sorted(self.books_on_sale, key=lambda book: book.price)
        return books_by_price

    def get_most_popular_book(self) -> list:
        """
        Return a list of book (books) with the highest rating.

        :return: list of Book objects
        """
        popular_books = sorted(self.books_on_sale, key=lambda book: book.rating)
        most_popular_books = []
        for book in self.books_on_sale:
            if book.rating == popular_books[-1].rating:
                most_popular_books.append(book)
        return most_popular_books