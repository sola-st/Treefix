class MockQuerySet:# pragma: no cover
    def filter(self, **kwargs):# pragma: no cover
        return [MockBook(User(), 'Sample Book')]  # Simulating filtering# pragma: no cover
    def __getitem__(self, item):# pragma: no cover
        return self if item is None else [] # pragma: no cover
class MockBook:# pragma: no cover
    def __init__(self, author, title):# pragma: no cover
        self.author = author# pragma: no cover
        self.title = title# pragma: no cover
    objects = MockQuerySet() # pragma: no cover
Book = MockBook # pragma: no cover
def get_books(limit=None, **filters):# pragma: no cover
    return Book.objects.filter(**filters)[:limit]  # Implementation of get_books function # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/12578908/separation-of-business-logic-and-data-access-in-django
from l3.Runtime import _l_
class Book:
   _l_(240)

   author = models.ForeignKey(User)
   _l_(236)
   title = models.CharField(max_length=125)
   _l_(237)

   class Meta:
      _l_(239)

      app_label = "library"
      _l_(238)
try:
   from library.models import Book
   _l_(242)

except ImportError:
   pass

def get_books(limit=None, **filters):
   _l_(244)

   """ simple service function for retrieving books can be widely extended """
   aux = Book.objects.filter(**filters)[:limit]  # list[:None] will return the entire list
   _l_(243)  # list[:None] will return the entire list
   return aux  # list[:None] will return the entire list
try:
   from library.services import get_books
   _l_(246)

except ImportError:
   pass

class BookListView(ListView):
   _l_(248)

   """ simple view, e.g. implement a _build and _apply filters function """
   queryset = get_books()
   _l_(247)

