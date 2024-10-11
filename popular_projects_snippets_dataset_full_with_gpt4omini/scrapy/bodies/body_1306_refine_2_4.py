from typing import Any, Dict # pragma: no cover
class NotConfigured(Exception): pass # pragma: no cover
class MockSettings: # pragma: no cover
    def __init__(self, config: Dict[str, Any]): # pragma: no cover
        self.config = config # pragma: no cover
    def getbool(self, key: str) -> bool: # pragma: no cover
        return self.config.get(key, False) # pragma: no cover
    def getint(self, key: str) -> int: # pragma: no cover
        return int(self.config.get(key, 0)) # pragma: no cover

settings = MockSettings({ 'RETRY_ENABLED': False, 'RETRY_TIMES': 5, 'RETRY_HTTP_CODES': ['500', '502', '503', '504'], 'RETRY_PRIORITY_ADJUST': 0 }) # pragma: no cover
NotConfigured = type('NotConfigured', (Exception,), {}) # pragma: no cover
self = type('Mock', (object,), { 'max_retry_times': 0, 'retry_http_codes': set(), 'priority_adjust': 0 }) # pragma: no cover

from typing import Any, Dict # pragma: no cover

class NotConfigured(Exception): pass # pragma: no cover
class MockSettings: # pragma: no cover
    def __init__(self, config: Dict[str, Any]): # pragma: no cover
        self.config = config # pragma: no cover
    def getbool(self, key: str) -> bool: # pragma: no cover
        return self.config.get(key, True) # pragma: no cover
 # Change default to True to avoid raising the exception # pragma: no cover
    def getint(self, key: str) -> int: # pragma: no cover
        return int(self.config.get(key, 0)) # pragma: no cover
settings = MockSettings({ 'RETRY_ENABLED': True, 'RETRY_TIMES': 5, 'RETRY_HTTP_CODES': ['500', '502', '503', '504'], 'RETRY_PRIORITY_ADJUST': 0 }) # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
setattr(self, 'max_retry_times', settings.getint('RETRY_TIMES')) # pragma: no cover
setattr(self, 'priority_adjust', settings.getint('RETRY_PRIORITY_ADJUST')) # pragma: no cover

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
