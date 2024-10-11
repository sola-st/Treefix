from unittest.mock import MagicMock # pragma: no cover

settings = MagicMock() # pragma: no cover
NotConfigured = Exception('Not Configured') # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
settings.getbool.return_value = False # pragma: no cover
settings.getint.side_effect = lambda x: {'RETRY_TIMES': 5, 'RETRY_PRIORITY_ADJUST': 1}.get(x, 0) # pragma: no cover
settings.getlist.return_value = ['500', '503', '502'] # pragma: no cover

from unittest.mock import MagicMock # pragma: no cover

settings = MagicMock() # pragma: no cover
NotConfigured = Exception('Not Configured') # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
settings.getbool.return_value = True # pragma: no cover
settings.getint.side_effect = lambda key: {'RETRY_TIMES': 5, 'RETRY_PRIORITY_ADJUST': 1}.get(key, 0) # pragma: no cover
settings.getlist.return_value = ['500', '502', '503'] # pragma: no cover

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
