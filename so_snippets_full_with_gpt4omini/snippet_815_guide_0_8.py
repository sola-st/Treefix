class MockBook: # pragma: no cover
    def __init__(self, author): # pragma: no cover
        self.author = author # pragma: no cover
class MockClass: # pragma: no cover
    def __init__(self, book): # pragma: no cover
        self.book = book # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/163823/can-list-display-in-a-django-modeladmin-display-attributes-of-foreignkey-field
from l3.Runtime import _l_
def book_author(self):
  _l_(2883)

  aux = self.book.author
  _l_(2882)
  return aux

