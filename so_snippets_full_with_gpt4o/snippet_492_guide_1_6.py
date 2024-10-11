from django.db import models # pragma: no cover
from django.views.generic import ListView # pragma: no cover

class MockForeignKey(models.ForeignKey): # pragma: no cover
    def __init__(self, to, on_delete=None): # pragma: no cover
        self.to = to # pragma: no cover
        self.on_delete = on_delete # pragma: no cover
class MockCharField(models.CharField): # pragma: no cover
    def __init__(self, max_length): # pragma: no cover
        self.max_length = max_length # pragma: no cover
class MockQuerySet: # pragma: no cover
    def filter(self, **kwargs): # pragma: no cover
        return self # pragma: no cover
    def __getitem__(self, key): # pragma: no cover
        return [] # pragma: no cover
class MockBook: # pragma: no cover
    objects = MockQuerySet() # pragma: no cover
Book = MockBook # pragma: no cover
def get_books(limit=None, **filters): # pragma: no cover
    return Book.objects.filter(**filters)[:limit] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/12578908/separation-of-business-logic-and-data-access-in-django
from l3.Runtime import _l_
class Book:
   _l_(12142)

   author = models.ForeignKey(User)
   _l_(12138)
   title = models.CharField(max_length=125)
   _l_(12139)

   class Meta:
      _l_(12141)

      app_label = "library"
      _l_(12140)
try:
   from library.models import Book
   _l_(12144)

except ImportError:
   pass

def get_books(limit=None, **filters):
   _l_(12146)

   """ simple service function for retrieving books can be widely extended """
   aux = Book.objects.filter(**filters)[:limit]  # list[:None] will return the entire list
   _l_(12145)  # list[:None] will return the entire list
   return aux  # list[:None] will return the entire list
try:
   from library.services import get_books
   _l_(12148)

except ImportError:
   pass

class BookListView(ListView):
   _l_(12150)

   """ simple view, e.g. implement a _build and _apply filters function """
   queryset = get_books()
   _l_(12149)

