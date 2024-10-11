import logging # pragma: no cover

logger = logging.getLogger(__name__) # pragma: no cover
type('Mock', (object,), {'push': lambda self, request: None, 'inc_value': lambda self, key, spider=None: None}) # pragma: no cover
self = type('Mock', (object,), {'dqs': None, 'logunser': True, 'spider': 'example_spider', 'stats': type('Mock', (object,), {})()}) # pragma: no cover
request = 'example_request' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/scheduler.py
from l3.Runtime import _l_
if self.dqs is None:
    _l_(20275)

    aux = False
    _l_(20274)
    exit(aux)
try:
    _l_(20285)

    self.dqs.push(request)
    _l_(20276)
except ValueError as e:
    _l_(20283)

    if self.logunser:
        _l_(20280)

        msg = ("Unable to serialize request: %(request)s - reason:"
               " %(reason)s - no more unserializable requests will be"
               " logged (stats being collected)")
        _l_(20277)
        logger.warning(msg, {'request': request, 'reason': e},
                       exc_info=True, extra={'spider': self.spider})
        _l_(20278)
        self.logunser = False
        _l_(20279)
    self.stats.inc_value('scheduler/unserializable', spider=self.spider)
    _l_(20281)
    aux = False
    _l_(20282)
    exit(aux)
else:
    aux = True
    _l_(20284)
    exit(aux)
