from typing import List # pragma: no cover
from urllib.parse import urlparse # pragma: no cover

links = [type('Link', (object,), {'url': 'http://example.com/page1'}), type('Link', (object,), {'url': 'http://example.com/page2'})] # pragma: no cover
self = type('Mock', (object,), {'_link_allowed': lambda self, x: True, 'canonicalize': True, 'link_extractor': type('MockLinkExtractor', (object,), {'_process_links': lambda self, links: links})()})() # pragma: no cover
canonicalize_url = lambda url: urlparse(url)._replace(scheme='https').geturl() # pragma: no cover

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
