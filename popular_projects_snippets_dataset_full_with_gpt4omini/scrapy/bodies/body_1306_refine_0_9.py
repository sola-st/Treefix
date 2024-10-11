from typing import Any, List, Set # pragma: no cover

class MockSettings:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.values = {'RETRY_ENABLED': False, 'RETRY_TIMES': 5, 'RETRY_HTTP_CODES': ['500', '502', '503', '504'], 'RETRY_PRIORITY_ADJUST': -1}# pragma: no cover
    def getbool(self, key: str) -> bool:# pragma: no cover
        return self.values.get(key, False)# pragma: no cover
    def getint(self, key: str) -> int:# pragma: no cover
        return int(self.values.get(key, 0))# pragma: no cover
    def getlist(self, key: str) -> List[str]:# pragma: no cover
        return self.values.get(key, [])# pragma: no cover
# pragma: no cover
settings = MockSettings() # pragma: no cover
class NotConfigured(Exception):# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
NotConfigured = NotConfigured # pragma: no cover
class Mock:# pragma: no cover
    max_retry_times = 0# pragma: no cover
    retry_http_codes = set()# pragma: no cover
    priority_adjust = 0# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover

from typing import Any, List, Set # pragma: no cover

class MockSettings:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.values = {'RETRY_ENABLED': False, 'RETRY_TIMES': 5, 'RETRY_HTTP_CODES': ['500', '502', '503', '504'], 'RETRY_PRIORITY_ADJUST': -1}# pragma: no cover
    def getbool(self, key: str) -> bool:# pragma: no cover
        return self.values.get(key, False)# pragma: no cover
    def getint(self, key: str) -> int:# pragma: no cover
        return int(self.values.get(key, 0))# pragma: no cover
    def getlist(self, key: str) -> List[str]:# pragma: no cover
        return self.values.get(key, [])# pragma: no cover
# pragma: no cover
settings = MockSettings() # pragma: no cover
class NotConfigured(Exception):# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
NotConfigured = NotConfigured # pragma: no cover
class Mock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.max_retry_times = 0# pragma: no cover
        self.retry_http_codes = set()# pragma: no cover
        self.priority_adjust = 0# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover

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
