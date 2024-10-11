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

from unittest.mock import Mock # pragma: no cover
from scrapy.exceptions import NotConfigured # pragma: no cover

settings = type('MockSettings', (object,), { # pragma: no cover
    'getbool': Mock(return_value=True), # pragma: no cover
    'getint': Mock(side_effect=lambda x: 3 if x == 'RETRY_TIMES' else 0), # pragma: no cover
    'getlist': Mock(return_value=['500', '502', '503', '504']) # pragma: no cover
})() # pragma: no cover
self = type('MockSelf', (object,), {'max_retry_times': None, 'retry_http_codes': None, 'priority_adjust': None})() # pragma: no cover

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
