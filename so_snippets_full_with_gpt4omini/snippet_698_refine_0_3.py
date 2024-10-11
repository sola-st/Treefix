client_id = 1 # pragma: no cover

class MockQuerySet:  # Mocking Django's QuerySet # pragma: no cover
    def __init__(self, data): self.data = data # pragma: no cover
    def filter(self, **kwargs): return MockQuerySet([d for d in self.data if all(getattr(d, k) == v for k, v in kwargs.items())]) # pragma: no cover
    def order_by(self, *args): return self.data if args[0] == 'check_in' else self.data[::-1] # pragma: no cover
class Reserved:  # Mocking the Reserved model # pragma: no cover
    pass
client_id = 1 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9834038/django-order-by-query-set-ascending-and-descending
from l3.Runtime import _l_
Reserved.objects.all().filter(client=client_id).order_by('check_in')
_l_(3477)

Reserved.objects.all().filter(client=client_id).order_by('-check_in')
_l_(3478)

