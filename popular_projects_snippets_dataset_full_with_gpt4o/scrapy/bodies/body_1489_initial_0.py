from typing import Any # pragma: no cover

url = 'http://example.com/path' # pragma: no cover
self = type('Mock', (object,), {'strip_url': lambda self, url, origin_only: (url.split('://')[0], url.split('://')[1].split('/')[0], '/'.join(url.split('://')[1].split('/')[1:]))})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
from l3.Runtime import _l_
"""Return serialized origin (scheme, host, path) for a request or response URL."""
aux = self.strip_url(url, origin_only=True)
_l_(17724)
exit(aux)
