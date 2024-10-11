import logging # pragma: no cover

class MockScheduler: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.dqs = None # pragma: no cover
        self.spider = 'mock_spider' # pragma: no cover
        self.logunser = True # pragma: no cover
        self.stats = type('MockStats', (object,), {'inc_value': lambda self, *args, **kwargs: None})() # pragma: no cover
 # pragma: no cover
    def push(self, request): # pragma: no cover
        raise ValueError('mock error') # pragma: no cover
 # pragma: no cover
self = MockScheduler() # pragma: no cover
logger = logging.getLogger('mock_logger') # pragma: no cover
request = 'mock_request' # pragma: no cover

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
