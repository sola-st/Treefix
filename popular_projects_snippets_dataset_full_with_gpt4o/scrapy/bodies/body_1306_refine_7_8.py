from typing import Any # pragma: no cover
from collections.abc import Callable # pragma: no cover
class NotConfigured(Exception): pass # pragma: no cover

class NotConfigured(Exception): pass # pragma: no cover
self = type('Mock', (object,), {'max_retry_times': None, 'retry_http_codes': None, 'priority_adjust': None})() # pragma: no cover

from typing import Any, List # pragma: no cover

class MockSettings: # pragma: no cover
    def getbool(self, key: str) -> bool: # pragma: no cover
        return True # pragma: no cover
    def getint(self, key: str) -> int: # pragma: no cover
        return 3 # pragma: no cover
    def getlist(self, key: str) -> List[str]: # pragma: no cover
        return ['500', '502', '503', '504'] # pragma: no cover
 # pragma: no cover
class NotConfigured(Exception): # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.max_retry_times = 0 # pragma: no cover
        self.retry_http_codes = set() # pragma: no cover
        self.priority_adjust = 0 # pragma: no cover
 # pragma: no cover
settings = MockSettings() # pragma: no cover
self = MockSelf() # pragma: no cover

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
