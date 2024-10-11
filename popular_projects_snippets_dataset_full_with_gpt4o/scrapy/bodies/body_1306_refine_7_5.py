from typing import Any # pragma: no cover
from collections.abc import Callable # pragma: no cover
class NotConfigured(Exception): pass # pragma: no cover

class NotConfigured(Exception): pass # pragma: no cover
self = type('Mock', (object,), {'max_retry_times': None, 'retry_http_codes': None, 'priority_adjust': None})() # pragma: no cover

from types import SimpleNamespace # pragma: no cover

settings = SimpleNamespace(getbool=lambda x: True if x == 'RETRY_ENABLED' else False, getint=lambda x: 3, getlist=lambda x: ['500', '502', '503', '504']) # pragma: no cover
class NotConfigured(Exception): pass # pragma: no cover
self = SimpleNamespace(max_retry_times=None, retry_http_codes=None, priority_adjust=None) # pragma: no cover

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
