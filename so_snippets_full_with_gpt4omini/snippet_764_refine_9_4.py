from dataclasses import dataclass, field # pragma: no cover

@dataclass# pragma: no cover
class User:# pragma: no cover
    income: float = field(default=None)# pragma: no cover
    category: str = field(default='') # pragma: no cover
User.objects = type('MockManager', (object,), {'filter': lambda self, *args, **kwargs: 'Filtered Users'}) # pragma: no cover

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

