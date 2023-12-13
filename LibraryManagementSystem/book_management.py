from typing import List, Union


class Book:
    def __init__(self, name: str, author: str, publication: str, book_arrival: str, quantity: int, price: int):
        self.name = name
        self.author = author
        self.publication = publication
        self.book_arrival = book_arrival
        self.quantity = quantity
        self.price = price
        self.book_lists = []

    def add_book(self) -> List:
        new_book = {
            "name": self.name,
            "author": self.author,
            "publication": self.publication,
            "book_arrival": self.book_arrival,
            "quantity": self.quantity,
            'price': self.price,
        }
        if not self.check_book_exists(new_book):
            self.book_lists.append(new_book)
            print("Book added")
            return self.book_lists
        else:
            print("Book exists")

    def check_book_exists(self, new_book: dict) -> bool:
        for book in self.book_lists:
            if book["name"] == new_book["name"] and book["author"] == new_book["author"]:
                return True
                break

    def update_book(self, name: str, **kwargs) -> Union[List, dict]:
        found = False
        for book in self.book_lists:
            if book["name"] == name:
                book['name'] = kwargs.get('name', book['name'])
                book['author'] = kwargs.get('author', book['author'])
                book['publication'] = kwargs.get('publication', book['publication'])
                book['price'] = kwargs.get('price', book['price'])
                book['quantity'] = kwargs.get('quantity', book['quantity'])
                found = True
                break

        if not found:
            print(f"{name} book not found in the book list")
        return book if found else self.book_lists

    def remove_book(self, name) -> List:
        if self.book_name_exists(name):
            book = next((book for book in self.book_lists if book['name'] == name), None)
            self.book_lists.remove(book)
            return self.book_lists
        else:
            print(f"{name} book doesn't exists in the list")

    def book_name_exists(self, name) -> bool:
        return any((book for book in self.book_lists if book["name"] == name))

    def display_books(self):
        print(self.book_lists)



