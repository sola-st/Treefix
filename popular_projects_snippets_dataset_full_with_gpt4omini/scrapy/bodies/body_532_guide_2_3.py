import datetime # pragma: no cover
import decimal # pragma: no cover
class Request: # pragma: no cover
    def __init__(self, method, url): # pragma: no cover
        self.method = method # pragma: no cover
        self.url = url # pragma: no cover
class Response: # pragma: no cover
    def __init__(self, status, url): # pragma: no cover
        self.status = status # pragma: no cover
        self.url = url # pragma: no cover
def is_item(o): return isinstance(o, dict) # pragma: no cover
class ItemAdapter: # pragma: no cover
    def __init__(self, item): self.item = item # pragma: no cover
    def asdict(self): return {'item': self.item} # pragma: no cover

o = set([1, 2, 3]) # pragma: no cover
self = type('Mock', (), {'DATE_FORMAT': '%Y-%m-%d', 'TIME_FORMAT': '%H:%M:%S'})() # pragma: no cover

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
