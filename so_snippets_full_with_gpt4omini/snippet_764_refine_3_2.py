from typing import List, Optional # pragma: no cover

class User:# pragma: no cover
    def __init__(self, income: Optional[float] = None, category: str = ''):# pragma: no cover
        self.income = income# pragma: no cover
        self.category = category# pragma: no cover
    # pragma: no cover
    @staticmethod# pragma: no cover
    def objects():# pragma: no cover
        return UserManager() # pragma: no cover
class UserManager:# pragma: no cover
    @staticmethod# pragma: no cover
    def filter(*args, **kwargs) -> List[User]:# pragma: no cover
        return ['filtered_users'] # pragma: no cover

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

