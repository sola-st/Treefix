from typing import Dict, Any, List # pragma: no cover

class MockSettings:# pragma: no cover
    def __init__(self, config: Dict[str, Any]):# pragma: no cover
        self.config = config# pragma: no cover
    # pragma: no cover
    def getbool(self, key: str) -> bool:# pragma: no cover
        return self.config.get(key, False)# pragma: no cover
    # pragma: no cover
    def getint(self, key: str) -> int:# pragma: no cover
        return self.config.get(key, 0)# pragma: no cover
    # pragma: no cover
    def getlist(self, key: str) -> List[int]:# pragma: no cover
        return self.config.get(key, [])# pragma: no cover
 # pragma: no cover
settings = MockSettings({# pragma: no cover
    'RETRY_ENABLED': False,# pragma: no cover
    'RETRY_TIMES': 5,# pragma: no cover
    'RETRY_HTTP_CODES': ['500', '502', '503', '504'],# pragma: no cover
    'RETRY_PRIORITY_ADJUST': 10# pragma: no cover
}) # pragma: no cover
class NotConfigured(Exception):# pragma: no cover
    pass # pragma: no cover
self = type('MockSelf', (object,), {'max_retry_times': None, 'retry_http_codes': None, 'priority_adjust': None})() # pragma: no cover

from typing import Dict, Any, List # pragma: no cover

class MockSettings:# pragma: no cover
    def __init__(self, config: Dict[str, Any]):# pragma: no cover
        self.config = config# pragma: no cover
# pragma: no cover
    def getbool(self, key: str) -> bool:# pragma: no cover
        return self.config.get(key, False)# pragma: no cover
# pragma: no cover
    def getint(self, key: str) -> int:# pragma: no cover
        return self.config.get(key, 0)# pragma: no cover
# pragma: no cover
    def getlist(self, key: str) -> List[int]:# pragma: no cover
        return list(map(int, self.config.get(key, [])))# pragma: no cover
 # pragma: no cover
settings = MockSettings({# pragma: no cover
    'RETRY_ENABLED': True,  # Set to True to avoid raising NotConfigured# pragma: no cover
    'RETRY_TIMES': 5,# pragma: no cover
    'RETRY_HTTP_CODES': ['500', '502', '503', '504'],# pragma: no cover
    'RETRY_PRIORITY_ADJUST': 10# pragma: no cover
}) # pragma: no cover
class NotConfigured(Exception):# pragma: no cover
    pass # pragma: no cover
self = type('MockSelf', (object,), {})() # pragma: no cover

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
