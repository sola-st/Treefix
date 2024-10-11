from unittest.mock import MagicMock # pragma: no cover

settings = MagicMock() # pragma: no cover
settings.getbool.return_value = False # pragma: no cover
settings.getint.return_value = 5 # pragma: no cover
settings.getlist.return_value = ['500', '404'] # pragma: no cover
NotConfigured = Exception('Configuration not set.') # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
setattr(self, 'max_retry_times', settings.getint('RETRY_TIMES')) # pragma: no cover
setattr(self, 'retry_http_codes', set(int(x) for x in settings.getlist('RETRY_HTTP_CODES'))) # pragma: no cover
setattr(self, 'priority_adjust', settings.getint('RETRY_PRIORITY_ADJUST')) # pragma: no cover

class NotConfigured(Exception):# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
NotConfigured = NotConfigured # pragma: no cover
class MockSettings:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.values = {'RETRY_ENABLED': True, 'RETRY_TIMES': 5, 'RETRY_HTTP_CODES': ['500', '404'], 'RETRY_PRIORITY_ADJUST': -1}# pragma: no cover
    def getbool(self, key: str) -> bool:# pragma: no cover
        return self.values.get(key, False)# pragma: no cover
    def getint(self, key: str) -> int:# pragma: no cover
        return int(self.values.get(key, 0))# pragma: no cover
# pragma: no cover
settings = MockSettings() # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
self.max_retry_times = settings.getint('RETRY_TIMES') # pragma: no cover
self.priority_adjust = settings.getint('RETRY_PRIORITY_ADJUST') # pragma: no cover

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
