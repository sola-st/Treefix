from scrapy.exceptions import NotConfigured # pragma: no cover

settings = type('Mock', (object,), {})() # pragma: no cover
settings.getbool = lambda key: True if key == 'RETRY_ENABLED' else None # pragma: no cover
settings.getint = lambda key: 5 if key in ['RETRY_TIMES', 'RETRY_PRIORITY_ADJUST'] else None # pragma: no cover
settings.getlist = lambda key: ['500', '502', '503'] if key == 'RETRY_HTTP_CODES' else [] # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover

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
