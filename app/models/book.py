import uuid


class Book:
    def __init__(self, title, author, pages):
        self.id = str(uuid.uuid4())[:8]
        self._title = title.title()
        self._author = author.title()
        self._pages = pages
        self._price = 0
        self._edition = 0
    
    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @property
    def pages(self):
        return self._pages
    
    @property
    def price(self):
        return self._price
    
    @property
    def edition(self):
        return self._edition
    
    @title.setter
    def title(self, value):
        self._title = value

    @author.setter
    def author(self, value):
        self._author = value

    @pages.setter
    def pages(self, value):
        self._pages = value
    
    @price.setter
    def price(self, value):
        self._price = value

    @edition.setter
    def edition(self, value):
        self._edition=value

    def to_dict(self):
        return {
            "id": self.id,
            "title": self._title,
            "author": self._author,
            "pages": self._pages,
            "price": self._price,
            "edition": self._edition
        }
    
    @classmethod
    def from_dict(cls, data):
        book = cls(data["title"], data["author"], data["pages"])
        book.id = data["id"]
        book._price = data["price"]
        book._edition = data["edition"]
        return book
    
    def __str__(self):
        return (
            f"[{self.id}] {self._title} — {self._author} | "
            f"Edição: {self._edition} | Páginas: {self._pages} | "
            f"Preço: R$ {self._price:.2f}"
        )