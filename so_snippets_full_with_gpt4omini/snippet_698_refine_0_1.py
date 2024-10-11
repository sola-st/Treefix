client_id = 1 # pragma: no cover

class MockQuerySet: # pragma: no cover
    def all(self): return self # pragma: no cover
    def filter(self, **kwargs): return self # pragma: no cover
    def order_by(self, *args): return self # pragma: no cover
class MockManager: # pragma: no cover
    def get_queryset(self): return MockQuerySet() # pragma: no cover
    def all(self): return self.get_queryset() # pragma: no cover
    def filter(self, **kwargs): return self.get_queryset().filter(**kwargs) # pragma: no cover
client_id = 1 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9834038/django-order-by-query-set-ascending-and-descending
from l3.Runtime import _l_
Reserved.objects.all().filter(client=client_id).order_by('check_in')
_l_(3477)

Reserved.objects.all().filter(client=client_id).order_by('-check_in')
_l_(3478)

