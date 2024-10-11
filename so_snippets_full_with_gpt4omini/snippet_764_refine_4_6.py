from dataclasses import dataclass # pragma: no cover
from typing import Optional, List # pragma: no cover

@dataclass# pragma: no cover
class User:# pragma: no cover
    income: Optional[float] = None# pragma: no cover
    category: str = ''# pragma: no cover
# pragma: no cover
def mock_filter(*args, **kwargs) -> List[User]:# pragma: no cover
    return []  # Simulates return of user query set# pragma: no cover
User.objects = type('MockManager', (object,), {'filter': mock_filter})() # pragma: no cover

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

