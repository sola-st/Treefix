from urllib.parse import urlparse # pragma: no cover

class Mock:# pragma: no cover
    def strip_url(self, url, origin_only=False):# pragma: no cover
        parsed_url = urlparse(url)# pragma: no cover
        return (parsed_url.scheme, parsed_url.netloc, parsed_url.path) if origin_only else url # pragma: no cover
self = Mock() # pragma: no cover
url = 'https://www.example.com/path/to/resource' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
from l3.Runtime import _l_
"""Return serialized origin (scheme, host, path) for a request or response URL."""
aux = self.strip_url(url, origin_only=True)
_l_(6501)
exit(aux)
