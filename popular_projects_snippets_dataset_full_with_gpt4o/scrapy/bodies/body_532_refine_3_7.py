import datetime # pragma: no cover
import decimal # pragma: no cover
from twisted.internet import defer # pragma: no cover
from itemadapter import ItemAdapter # pragma: no cover

o = set() # pragma: no cover
self = type('Mock', (object,), {'DATE_FORMAT': '%Y-%m-%d', 'TIME_FORMAT': '%H:%M:%S'})() # pragma: no cover

import datetime # pragma: no cover
import decimal # pragma: no cover
from twisted.internet import defer # pragma: no cover
from itemadapter import ItemAdapter # pragma: no cover
from scrapy.http import Request, Response # pragma: no cover

 # pragma: no cover
o = set() # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    DATE_FORMAT = '%Y-%m-%d' # pragma: no cover
    TIME_FORMAT = '%H:%M:%S' # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover
 # pragma: no cover
def is_item(x): return True # pragma: no cover
 # pragma: no cover
class MockItemAdapter: # pragma: no cover
    def __init__(self, item): # pragma: no cover
        pass # pragma: no cover
    def asdict(self): # pragma: no cover
        return {'key': 'value'} # pragma: no cover
 # pragma: no cover
ItemAdapter = MockItemAdapter # pragma: no cover
 # pragma: no cover
class MockRequest: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.method = 'GET' # pragma: no cover
        self.url = 'http://example.com' # pragma: no cover
 # pragma: no cover
Request = MockRequest # pragma: no cover
 # pragma: no cover
class MockResponse: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.status = 200 # pragma: no cover
        self.url = 'http://example.com' # pragma: no cover
 # pragma: no cover
Response = MockResponse # pragma: no cover

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
