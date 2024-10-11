ListView = type('MockListView', (object,), {}) # pragma: no cover
User = type('MockUser', (object,), {}) # pragma: no cover
models = type('MockModels', (object,), {'ForeignKey': type('MockForeignKey', (object,), {}), 'CharField': type('MockCharField', (object,), {})}) # pragma: no cover

class MockForeignKey:# pragma: no cover
    def __init__(self, *args, **kwargs): pass # pragma: no cover
class MockCharField:# pragma: no cover
    def __init__(self, max_length): pass # pragma: no cover
ListView = type('MockListView', (object,), {}) # pragma: no cover
models = type('MockModels', (object,), {'ForeignKey': MockForeignKey, 'CharField': MockCharField}) # pragma: no cover
User = type('MockUser', (object,), {}) # pragma: no cover

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

