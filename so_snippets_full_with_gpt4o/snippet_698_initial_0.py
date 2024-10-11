from typing import List # pragma: no cover
from dataclasses import dataclass # pragma: no cover

@dataclass# pragma: no cover
class Client:# pragma: no cover
    id: int # pragma: no cover
@dataclass# pragma: no cover
class Reservation:# pragma: no cover
    client: int# pragma: no cover
    check_in: str # pragma: no cover
class MockQuerySet:# pragma: no cover
    def __init__(self, data: List[Reservation]):# pragma: no cover
        self.data = data# pragma: no cover
    def all(self):# pragma: no cover
        return self# pragma: no cover
    def filter(self, **kwargs):# pragma: no cover
        client_id = kwargs.get('client')# pragma: no cover
        return MockQuerySet([item for item in self.data if item.client == client_id])# pragma: no cover
    def order_by(self, field_name):# pragma: no cover
        reverse = field_name.startswith('-')# pragma: no cover
        field_name = field_name.lstrip('-')# pragma: no cover
        self.data.sort(key=lambda x: getattr(x, field_name), reverse=reverse)# pragma: no cover
        return self# pragma: no cover
    def __repr__(self):# pragma: no cover
        return f'MockQuerySet(data={self.data})' # pragma: no cover
Reserved = type('Mock', (object,), {'objects': MockQuerySet([Reservation(client=1, check_in='2023-10-01'), Reservation(client=2, check_in='2023-10-05'), Reservation(client=1, check_in='2023-10-03')])}) # pragma: no cover
client_id = 1 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9834038/django-order-by-query-set-ascending-and-descending
from l3.Runtime import _l_
Reserved.objects.all().filter(client=client_id).order_by('check_in')
_l_(14413)

Reserved.objects.all().filter(client=client_id).order_by('-check_in')
_l_(14414)

