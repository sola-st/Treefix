class User:# pragma: no cover
    def __init__(self, income=None, category=''): self.income = income; self.category = category# pragma: no cover
    objects = type('MockManager', (object,), {'filter': lambda self, *args, **kwargs: [User(6000, 'income'), User(None, 'income') if kwargs.get('category') == 'income' else None]})() # pragma: no cover

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

