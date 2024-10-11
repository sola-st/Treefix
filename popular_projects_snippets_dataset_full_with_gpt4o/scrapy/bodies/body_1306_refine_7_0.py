from typing import Any # pragma: no cover
from collections.abc import Callable # pragma: no cover
class NotConfigured(Exception): pass # pragma: no cover

class NotConfigured(Exception): pass # pragma: no cover
self = type('Mock', (object,), {'max_retry_times': None, 'retry_http_codes': None, 'priority_adjust': None})() # pragma: no cover

class NotConfigured(Exception): pass # pragma: no cover

settings = type('Mock', (object,), { # pragma: no cover
    'getbool': lambda s, k: True if k == 'RETRY_ENABLED' else False, # pragma: no cover
    'getint': lambda s, k: 3 if k == 'RETRY_TIMES' else 0, # pragma: no cover
    'getlist': lambda s, k: ['500', '502', '503', '504'] # pragma: no cover
})() # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
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
