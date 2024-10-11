from urllib.parse import urlparse, urlunparse # pragma: no cover

def canonicalize_url(url, keep_fragments):# pragma: no cover
    parsed_url = urlparse(url)# pragma: no cover
    if not keep_fragments:# pragma: no cover
        parsed_url = parsed_url._replace(fragment='')# pragma: no cover
    return urlunparse(parsed_url) # pragma: no cover
link = type('Mock', (object,), {'url': 'http://example.com/path/to/resource#fragment'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/linkextractors/lxmlhtml.py
from l3.Runtime import _l_
aux = canonicalize_url(link.url, keep_fragments=True)
_l_(17579)
exit(aux)
