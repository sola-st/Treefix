from urllib.parse import urlparse, urlunparse # pragma: no cover

def canonicalize_url(url, keep_fragments=False): # pragma: no cover
    parsed_url = urlparse(url) # pragma: no cover
    if not keep_fragments: # pragma: no cover
        return urlunparse(parsed_url._replace(fragment='')) # pragma: no cover
    return url # pragma: no cover
link = type('Mock', (object,), {'url': 'https://example.com/path?query=1#fragment'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/linkextractors/lxmlhtml.py
from l3.Runtime import _l_
aux = canonicalize_url(link.url, keep_fragments=True)
_l_(6810)
exit(aux)
