import datetime # pragma: no cover
import decimal # pragma: no cover
from twisted.internet import defer # pragma: no cover

o = {1, 2, 3} # pragma: no cover
self = type('MockSelf', (), {'DATE_FORMAT': '%Y-%m-%d', 'TIME_FORMAT': '%H:%M:%S'})() # pragma: no cover
datetime = type('MockDateTime', (object,), {'datetime': datetime.datetime, 'date': datetime.date, 'time': datetime.time}) # pragma: no cover
decimal = decimal.Decimal # pragma: no cover
defer = type('MockDeferred', (object,), {}); defer.Deferred = type('MockDeferredObject', (object,), {}) # pragma: no cover
is_item = lambda x: True # pragma: no cover
ItemAdapter = type('ItemAdapter', (object,), {'asdict': lambda self: {'key': 'value'}}) # pragma: no cover
Request = type('MockRequest', (object,), {'method': 'GET', 'url': 'http://example.com'}) # pragma: no cover
Response = type('MockResponse', (object,), {'status': 200, 'url': 'http://example.com'}) # pragma: no cover

import datetime # pragma: no cover
import decimal # pragma: no cover
from twisted.internet import defer # pragma: no cover

o = datetime.datetime(2024, 7, 25, 5, 26, 3) # pragma: no cover
self = type('MockSelf', (), {'DATE_FORMAT': '%Y-%m-%d', 'TIME_FORMAT': '%H:%M:%S'})() # pragma: no cover
decimal = decimal.Decimal # pragma: no cover
defer = type('MockDeferred', (object,), {'Deferred': lambda: 'Deferred Object'}) # pragma: no cover
is_item = lambda x: isinstance(x, dict) # pragma: no cover
ItemAdapter = type('ItemAdapter', (object,), {'__init__': lambda self, obj: None, 'asdict': lambda self: {'mock_item': 'value'}}) # pragma: no cover
Request = type('MockRequest', (object,), {'method': 'GET', 'url': 'http://example.com'}) # pragma: no cover
Response = type('MockResponse', (object,), {'status': 200, 'url': 'http://example.com'}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/serialize.py
from l3.Runtime import _l_
if isinstance(o, set):
    _l_(7555)

    aux = list(o)
    _l_(7554)
    exit(aux)
if isinstance(o, datetime.datetime):
    _l_(7557)

    aux = o.strftime(f"{self.DATE_FORMAT} {self.TIME_FORMAT}")
    _l_(7556)
    exit(aux)
if isinstance(o, datetime.date):
    _l_(7559)

    aux = o.strftime(self.DATE_FORMAT)
    _l_(7558)
    exit(aux)
if isinstance(o, datetime.time):
    _l_(7561)

    aux = o.strftime(self.TIME_FORMAT)
    _l_(7560)
    exit(aux)
if isinstance(o, decimal.Decimal):
    _l_(7563)

    aux = str(o)
    _l_(7562)
    exit(aux)
if isinstance(o, defer.Deferred):
    _l_(7565)

    aux = str(o)
    _l_(7564)
    exit(aux)
if is_item(o):
    _l_(7567)

    aux = ItemAdapter(o).asdict()
    _l_(7566)
    exit(aux)
if isinstance(o, Request):
    _l_(7569)

    aux = f"<{type(o).__name__} {o.method} {o.url}>"
    _l_(7568)
    exit(aux)
if isinstance(o, Response):
    _l_(7571)

    aux = f"<{type(o).__name__} {o.status} {o.url}>"
    _l_(7570)
    exit(aux)
aux = super().default(o)
_l_(7572)
exit(aux)
