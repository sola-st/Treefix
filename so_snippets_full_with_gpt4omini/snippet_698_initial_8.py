class MockClient: pass # pragma: no cover
client_id = MockClient() # pragma: no cover
class ReservedManager:# pragma: no cover
    def filter(self, client):# pragma: no cover
        return self# pragma: no cover
    def order_by(self, order):# pragma: no cover
        return self # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9834038/django-order-by-query-set-ascending-and-descending
from l3.Runtime import _l_
Reserved.objects.all().filter(client=client_id).order_by('check_in')
_l_(3477)

Reserved.objects.all().filter(client=client_id).order_by('-check_in')
_l_(3478)

