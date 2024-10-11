from collections import defaultdict # pragma: no cover

class NotConfigured(Exception): pass # pragma: no cover
class Mock: # pragma: no cover
    def getbool(self, key): # pragma: no cover
        return False # pragma: no cover
    def getint(self, key): # pragma: no cover
        return 3 # pragma: no cover
    def getlist(self, key): # pragma: no cover
        return ['500', '502', '503'] # pragma: no cover
settings = Mock() # pragma: no cover
self = type('MockSelf', (object,), {'max_retry_times': 0, 'retry_http_codes': set(), 'priority_adjust': 0})() # pragma: no cover

class NotConfigured(Exception): pass # pragma: no cover

class MockSettings:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.values = {# pragma: no cover
            'RETRY_ENABLED': True,# pragma: no cover
            'RETRY_TIMES': 5,# pragma: no cover
            'RETRY_HTTP_CODES': ['500', '502', '503'],# pragma: no cover
            'RETRY_PRIORITY_ADJUST': 1# pragma: no cover
        }# pragma: no cover
    # pragma: no cover
    def getbool(self, key):# pragma: no cover
        return self.values.get(key, False)# pragma: no cover
    # pragma: no cover
    def getint(self, key):# pragma: no cover
        return self.values.get(key, 0)# pragma: no cover
    # pragma: no cover
    def getlist(self, key):# pragma: no cover
        return self.values.get(key, []) # pragma: no cover
settings = MockSettings() # pragma: no cover
self = type('MockSelf', (object,), {})() # pragma: no cover
self.max_retry_times = settings.getint('RETRY_TIMES') # pragma: no cover
self.retry_http_codes = set(int(x) for x in settings.getlist('RETRY_HTTP_CODES')) # pragma: no cover
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
