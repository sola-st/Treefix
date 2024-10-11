from django.db import models # pragma: no cover

class MockQuerySet:# pragma: no cover
    def filter(self, *args, **kwargs):# pragma: no cover
        return 'Mocked QuerySet Result' # pragma: no cover
class MockManager:# pragma: no cover
    objects = MockQuerySet() # pragma: no cover
class User(MockManager):# pragma: no cover
    income = models.IntegerField(null=True)# pragma: no cover
    category = models.CharField(max_length=255) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6567831/how-to-perform-or-condition-in-django-queryset
from l3.Runtime import _l_
try:
    from django.db.models import Q
    _l_(13008)

except ImportError:
    pass
User.objects.filter(Q(income__gte=5000) | Q(income__isnull=True),category='income')
_l_(13009)

