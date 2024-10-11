class MockBook: pass # pragma: no cover
class Mock: pass # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/163823/can-list-display-in-a-django-modeladmin-display-attributes-of-foreignkey-field
from l3.Runtime import _l_
def book_author(self):
  _l_(2883)

  aux = self.book.author
  _l_(2882)
  return aux

