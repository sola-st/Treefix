from unittest.mock import MagicMock # pragma: no cover

settings = MagicMock() # pragma: no cover
settings.getbool.return_value = False # pragma: no cover
settings.getint.return_value = 3 # pragma: no cover
settings.getlist.return_value = ['500', '502', '503'] # pragma: no cover
NotConfigured = Exception('Configuration not set') # pragma: no cover
self = type('MockSelf', (object,), {'max_retry_times': None, 'retry_http_codes': None, 'priority_adjust': None})() # pragma: no cover

from unittest.mock import MagicMock # pragma: no cover

settings = MagicMock() # pragma: no cover
settings.getbool.return_value = True # pragma: no cover
settings.getint.return_value = 3 # pragma: no cover
settings.getlist.return_value = ['500', '502', '503'] # pragma: no cover
class NotConfigured(Exception): pass # pragma: no cover
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
