from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy.settings import Settings # pragma: no cover

settings = Settings() # pragma: no cover
settings.set('RETRY_ENABLED', False) # pragma: no cover
settings.set('RETRY_TIMES', 5) # pragma: no cover
settings.set('RETRY_HTTP_CODES', ['500', '502', '503']) # pragma: no cover
settings.set('RETRY_PRIORITY_ADJUST', 0) # pragma: no cover
self = type('MockObject', (object,), {})() # pragma: no cover
self.max_retry_times = None # pragma: no cover
self.retry_http_codes = None # pragma: no cover
self.priority_adjust = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/retry.py
from l3.Runtime import _l_
if not settings.getbool('RETRY_ENABLED'):
    _l_(7912)

    raise NotConfigured
    _l_(7911)
self.max_retry_times = settings.getint('RETRY_TIMES')
_l_(7913)
self.retry_http_codes = set(int(x) for x in settings.getlist('RETRY_HTTP_CODES'))
_l_(7914)
self.priority_adjust = settings.getint('RETRY_PRIORITY_ADJUST')
_l_(7915)
