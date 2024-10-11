 # pragma: no cover
class MockQuerySet: # pragma: no cover
    def filter(self, *args, **kwargs): return f'Mock filter applied with args: {args}, kwargs: {kwargs}' # pragma: no cover
 # pragma: no cover
class MockManager: # pragma: no cover
    def __getattr__(self, name): # pragma: no cover
        if name == 'filter': # pragma: no cover
            return MockQuerySet().filter # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6567831/how-to-perform-or-condition-in-django-queryset
from l3.Runtime import _l_
try:
    from django.db.models import Q
    _l_(1343)

except ImportError:
    pass
User.objects.filter(Q(income__gte=5000) | Q(income__isnull=True),category='income')
_l_(1344)

