from types import SimpleNamespace # pragma: no cover

settings = SimpleNamespace(getbool=lambda x: False, getint=lambda x: 5, getlist=lambda x: ['500', '502', '503']) # pragma: no cover
NotConfigured = type('NotConfigured', (Exception,), {}) # pragma: no cover
self = SimpleNamespace(max_retry_times=None, retry_http_codes=None, priority_adjust=None) # pragma: no cover

from scrapy.exceptions import NotConfigured # pragma: no cover

settings = type('MockSettings', (object,), { 'getbool': lambda self, x: True, 'getint': lambda self, x: 3, 'getlist': lambda self, x: ['500', '502', '503'] })() # pragma: no cover
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
