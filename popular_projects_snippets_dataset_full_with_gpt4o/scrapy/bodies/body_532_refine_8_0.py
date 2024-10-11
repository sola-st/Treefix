import datetime # pragma: no cover
import decimal # pragma: no cover
from twisted.internet import defer # pragma: no cover

o = set([1, 2, 3]) # pragma: no cover
self = type('Mock', (object,), {'DATE_FORMAT': '%Y-%m-%d', 'TIME_FORMAT': '%H:%M:%S'})() # pragma: no cover
is_item = lambda x: hasattr(x, 'item') # pragma: no cover
ItemAdapter = type('ItemAdapter', (object,), {'__init__': lambda self, o: None, 'asdict': lambda self: {'key': 'value'}}) # pragma: no cover
Request = type('Request', (object,), {'method': 'GET', 'url': 'http://example.com'}) # pragma: no cover
Response = type('Response', (object,), {'status': 200, 'url': 'http://example.com'}) # pragma: no cover

import datetime # pragma: no cover
import decimal # pragma: no cover
from twisted.internet import defer # pragma: no cover

o = type('MockObject', (object,), {})() # pragma: no cover
self = type('MockSelf', (object,), {'DATE_FORMAT': '%Y-%m-%d', 'TIME_FORMAT': '%H:%M:%S'})() # pragma: no cover
o = set() # pragma: no cover
datetime.datetime = type('datetime', (object,), {'strftime': lambda self, format: '2023-10-10 12:00:00'})() # pragma: no cover
datetime.date = type('date', (object,), {'strftime': lambda self, format: '2023-10-10'})() # pragma: no cover
datetime.time = type('time', (object,), {'strftime': lambda self, format: '12:00:00'})() # pragma: no cover
decimal.Decimal = decimal.Decimal('10.5') # pragma: no cover
defer.Deferred = type('Deferred', (object,), {'__str__': lambda self: 'Deferred'})() # pragma: no cover
def is_item(obj): return False # pragma: no cover
ItemAdapter = type('ItemAdapter', (object,), {'__init__': lambda self, obj: None, 'asdict': lambda self: {'key': 'value'}}) # pragma: no cover
Request = type('Request', (object,), {'__init__': lambda self: None, 'method': 'GET', 'url': 'http://example.com'})() # pragma: no cover
Response = type('Response', (object,), {'__init__': lambda self: None, 'status': 200, 'url': 'http://example.com'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/serialize.py
from l3.Runtime import _l_
if isinstance(o, set):
    _l_(17981)

    aux = list(o)
    _l_(17980)
    exit(aux)
if isinstance(o, datetime.datetime):
    _l_(17983)

    aux = o.strftime(f"{self.DATE_FORMAT} {self.TIME_FORMAT}")
    _l_(17982)
    exit(aux)
if isinstance(o, datetime.date):
    _l_(17985)

    aux = o.strftime(self.DATE_FORMAT)
    _l_(17984)
    exit(aux)
if isinstance(o, datetime.time):
    _l_(17987)

    aux = o.strftime(self.TIME_FORMAT)
    _l_(17986)
    exit(aux)
if isinstance(o, decimal.Decimal):
    _l_(17989)

    aux = str(o)
    _l_(17988)
    exit(aux)
if isinstance(o, defer.Deferred):
    _l_(17991)

    aux = str(o)
    _l_(17990)
    exit(aux)
if is_item(o):
    _l_(17993)

    aux = ItemAdapter(o).asdict()
    _l_(17992)
    exit(aux)
if isinstance(o, Request):
    _l_(17995)

    aux = f"<{type(o).__name__} {o.method} {o.url}>"
    _l_(17994)
    exit(aux)
if isinstance(o, Response):
    _l_(17997)

    aux = f"<{type(o).__name__} {o.status} {o.url}>"
    _l_(17996)
    exit(aux)
aux = super().default(o)
_l_(17998)
exit(aux)
