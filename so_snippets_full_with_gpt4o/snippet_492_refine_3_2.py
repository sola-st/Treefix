from django.db import models # pragma: no cover
from django.views.generic import ListView # pragma: no cover

ListView = type('Mock', (object,), {}) # pragma: no cover
models = type('Mock', (object,), {'ForeignKey': lambda *args, **kwargs: None, 'CharField': lambda *args, **kwargs: None}) # pragma: no cover
User = type('Mock', (object,), {}) # pragma: no cover

from django.db import models # pragma: no cover
from django.views.generic import ListView # pragma: no cover

ListView = type('Mock', (object,), {}) # pragma: no cover
models = type('Mock', (object,), {'ForeignKey': type('Mock', (object,), {'__init__': lambda self, model: None}), 'CharField': type('Mock', (object,), {'__init__': lambda self, max_length: None})}) # pragma: no cover
User = type('Mock', (object,), {}) # pragma: no cover
sys.modules['library'] = type('Mock', (object,), {'models': type('Mock', (object,), {'Book': type('Book', (object,), {'author': None, 'title': None, 'Meta': type('Meta', (object,), {'app_label': 'library'})})}), 'services': type('Mock', (object,), {'get_books': lambda limit=None, **filters: []})}) # pragma: no cover

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

