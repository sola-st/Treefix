import logging # pragma: no cover
from collections import deque # pragma: no cover

class MockStats(object):# pragma: no cover
    def inc_value(self, key, spider=None): pass # pragma: no cover
class MockDQS(object):# pragma: no cover
    def __init__(self):# pragma: no cover
        self.queue = deque()# pragma: no cover
    def push(self, request):# pragma: no cover
        if not isinstance(request, dict):# pragma: no cover
            raise ValueError('Request is non-serializable')# pragma: no cover
        self.queue.append(request) # pragma: no cover
self = type('Mock', (), {'dqs': MockDQS(), 'logunser': True, 'spider': 'mock_spider', 'stats': MockStats()})() # pragma: no cover
request = {'data': 'test_request'} # pragma: no cover
logger = logging.getLogger('mock_logger') # pragma: no cover

import logging # pragma: no cover
from collections import deque # pragma: no cover

class MockStats(object):# pragma: no cover
    def __init__(self):# pragma: no cover
        self.stats = {}# pragma: no cover
    def inc_value(self, key, spider=None):# pragma: no cover
        self.stats[key] = self.stats.get(key, 0) + 1 # pragma: no cover
class MockDQS(object):# pragma: no cover
    def __init__(self):# pragma: no cover
        self.queue = deque()# pragma: no cover
    def push(self, request):# pragma: no cover
        if not isinstance(request, dict):# pragma: no cover
            raise ValueError('Request is non-serializable')# pragma: no cover
        self.queue.append(request) # pragma: no cover
self = type('Mock', (), {'dqs': MockDQS(), 'logunser': True, 'spider': 'mock_spider', 'stats': MockStats()})() # pragma: no cover
request = {'data': 'test_request'} # pragma: no cover
logger = logging.getLogger('mock_logger')# pragma: no cover
logger.setLevel(logging.WARNING)# pragma: no cover
handler = logging.StreamHandler()# pragma: no cover
logger.addHandler(handler) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/scheduler.py
from l3.Runtime import _l_
if self.dqs is None:
    _l_(9168)

    aux = False
    _l_(9167)
    exit(aux)
try:
    _l_(9178)

    self.dqs.push(request)
    _l_(9169)
except ValueError as e:
    _l_(9176)

    if self.logunser:
        _l_(9173)

        msg = ("Unable to serialize request: %(request)s - reason:"
               " %(reason)s - no more unserializable requests will be"
               " logged (stats being collected)")
        _l_(9170)
        logger.warning(msg, {'request': request, 'reason': e},
                       exc_info=True, extra={'spider': self.spider})
        _l_(9171)
        self.logunser = False
        _l_(9172)
    self.stats.inc_value('scheduler/unserializable', spider=self.spider)
    _l_(9174)
    aux = False
    _l_(9175)
    exit(aux)
else:
    aux = True
    _l_(9177)
    exit(aux)
