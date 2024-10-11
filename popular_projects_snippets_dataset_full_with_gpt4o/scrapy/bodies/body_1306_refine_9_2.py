from scrapy.exceptions import NotConfigured # pragma: no cover
class MockSettings: # pragma: no cover
    def getbool(self, key): # pragma: no cover
        return key == 'RETRY_ENABLED' and False # pragma: no cover
    def getint(self, key): # pragma: no cover
        if key == 'RETRY_TIMES': # pragma: no cover
            return 2 # pragma: no cover
        if key == 'RETRY_PRIORITY_ADJUST': # pragma: no cover
            return -1 # pragma: no cover
        return 0 # pragma: no cover
    def getlist(self, key): # pragma: no cover
        if key == 'RETRY_HTTP_CODES': # pragma: no cover
            return ['500', '502', '503', '504'] # pragma: no cover
        return [] # pragma: no cover

settings = MockSettings() # pragma: no cover
NotConfigured = type('NotConfigured', (Exception,), {}) # pragma: no cover
self = type('SelfMock', (object,), {})() # pragma: no cover

from scrapy.exceptions import NotConfigured # pragma: no cover
from unittest.mock import MagicMock # pragma: no cover

settings = type('Mock', (object,), { # pragma: no cover
    'getbool': MagicMock(return_value=True),  # Ensures RETRY_ENABLED is True # pragma: no cover
    'getint': MagicMock(side_effect=lambda k: 3 if k == 'RETRY_TIMES' else -1), # pragma: no cover
    'getlist': MagicMock(return_value=['500', '502', '503', '504']) # pragma: no cover
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
