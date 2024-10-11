from typing import List # pragma: no cover
from urllib.parse import urlparse, urlunparse, urlencode # pragma: no cover

links = [type('Link', (object,), {'url': 'http://example.com'})()] # pragma: no cover
self = type('Mock', (object,), { '_link_allowed': lambda x: True, 'canonicalize': True, 'link_extractor': type('LinkExtractor', (object,), {'_process_links': lambda self, links: links})() })() # pragma: no cover
def canonicalize_url(url: str) -> str: parsed_url = urlparse(url); query_string = urlencode(sorted(urlparse(url).query.split('&'))); return urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, query_string, parsed_url.fragment)) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/linkextractors/lxmlhtml.py
from l3.Runtime import _l_
links = [x for x in links if self._link_allowed(x)]
_l_(18406)
if self.canonicalize:
    _l_(18409)

    for link in links:
        _l_(18408)

        link.url = canonicalize_url(link.url)
        _l_(18407)
links = self.link_extractor._process_links(links)
_l_(18410)
aux = links
_l_(18411)
exit(aux)
