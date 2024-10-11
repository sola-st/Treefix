class NotConfigured(Exception): pass # pragma: no cover
from typing import Any, Dict # pragma: no cover

settings = type('MockSettings', (object,), {'getbool': lambda self, k: False, 'getint': lambda self, k: 3, 'getlist': lambda self, k: ['500', '502', '503', '504']})() # pragma: no cover
self = type('MockSelf', (object,), {'max_retry_times': 0, 'retry_http_codes': set(), 'priority_adjust': 0})() # pragma: no cover

from scrapy.exceptions import NotConfigured # pragma: no cover

settings = type('MockSettings', (object,), { # pragma: no cover
    'getbool': lambda self, k: True,  # Change return value to True to avoid raising NotConfigured # pragma: no cover
    'getint': lambda self, k: 3, # pragma: no cover
    'getlist': lambda self, k: ['500', '502', '503', '504'] # pragma: no cover
})() # pragma: no cover
 # pragma: no cover
self = type('MockSelf', (object,), { # pragma: no cover
    'max_retry_times': 0, # pragma: no cover
    'retry_http_codes': set(), # pragma: no cover
    'priority_adjust': 0 # pragma: no cover
})() # pragma: no cover

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
