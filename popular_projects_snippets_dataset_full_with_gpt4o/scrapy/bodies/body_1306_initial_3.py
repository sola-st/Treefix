from collections import defaultdict # pragma: no cover
from typing import Any # pragma: no cover

settings = type('MockSettings', (object,), { # pragma: no cover
    'getbool': lambda self, key: True, # pragma: no cover
    'getint': lambda self, key: 3, # pragma: no cover
    'getlist': lambda self, key: [500, 502, 503, 504] # pragma: no cover
})() # pragma: no cover
class NotConfigured(Exception): # pragma: no cover
    pass # pragma: no cover
self = type('MockSelf', (object,), {})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/retry.py
from l3.Runtime import _l_
if not settings.getbool('RETRY_ENABLED'):
    _l_(18876)

    raise NotConfigured
    _l_(18875)
self.max_retry_times = settings.getint('RETRY_TIMES')
_l_(18877)
self.retry_http_codes = set(int(x) for x in settings.getlist('RETRY_HTTP_CODES'))
_l_(18878)
self.priority_adjust = settings.getint('RETRY_PRIORITY_ADJUST')
_l_(18879)
