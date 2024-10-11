from unittest.mock import MagicMock # pragma: no cover

response = MagicMock(status=500) # pragma: no cover
self = type('Mock', (object,), {'_parse_cachecontrol': lambda self, cachedresponse: b'no-cache'})() # pragma: no cover
cachedresponse = b'cached response' # pragma: no cover

from unittest.mock import MagicMock # pragma: no cover

response = MagicMock(status=500) # pragma: no cover
self = type('Mock', (object,), {'_parse_cachecontrol': lambda self, cachedresponse: b'no-cache'})() # pragma: no cover
cachedresponse = b'cached response' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/httpcache.py
# Use the cached response if the new response is a server error,
# as long as the old response didn't specify must-revalidate.
from l3.Runtime import _l_
if response.status >= 500:
    _l_(7494)

    cc = self._parse_cachecontrol(cachedresponse)
    _l_(7491)
    if b'must-revalidate' not in cc:
        _l_(7493)

        aux = True
        _l_(7492)
        exit(aux)
aux = response.status == 304
_l_(7495)
exit(aux)
