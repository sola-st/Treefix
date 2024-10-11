class MockResponse:# pragma: no cover
    def __init__(self, status):# pragma: no cover
        self.status = status # pragma: no cover
class Mock:# pragma: no cover
    def _parse_cachecontrol(self, cached_response):# pragma: no cover
        return b'no-cache' # pragma: no cover
response = MockResponse(500) # pragma: no cover
self = Mock() # pragma: no cover
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
