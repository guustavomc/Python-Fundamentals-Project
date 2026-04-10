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
    
    @price.setter
    def price(self, value):
        self._price = value

    @edition.setter
    def edition(self, value):
        self._edition=value
