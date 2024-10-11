from django.db import models # pragma: no cover
from django.views.generic import ListView # pragma: no cover

models = type('Mock', (object,), { 'ForeignKey': lambda User, on_delete: None, 'CharField': lambda max_length: None }) # pragma: no cover
User = type('User', (object,), {}) # pragma: no cover
ListView = type('ListView', (object,), { 'queryset': None }) # pragma: no cover

from django.db import models # pragma: no cover
from django.views.generic import ListView # pragma: no cover

User = type('MockUser', (object,), {}) # pragma: no cover
models = type('MockModels', (object,), {'ForeignKey': lambda to, on_delete: None, 'CharField': lambda max_length: None}) # pragma: no cover
ListView = type('MockListView', (object,), {'queryset': None}) # pragma: no cover

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

