from urllib.parse import urlparse, urlunparse # pragma: no cover

class MockLink:# pragma: no cover
    def __init__(self, url):# pragma: no cover
        self.url = url# pragma: no cover
# pragma: no cover
links = [MockLink('http://example.com/1'), MockLink('http://example.com/2'), MockLink('http://example.com/3')] # pragma: no cover
class Mock:# pragma: no cover
    def _link_allowed(self, link):# pragma: no cover
        return True# pragma: no cover
    @property# pragma: no cover
    def canonicalize(self):# pragma: no cover
        return True# pragma: no cover
    @property# pragma: no cover
    def link_extractor(self):# pragma: no cover
        return self# pragma: no cover
    def _process_links(self, links):# pragma: no cover
        return links# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
def canonicalize_url(url):# pragma: no cover
    parsed_url = urlparse(url)# pragma: no cover
    return urlunparse(parsed_url._replace(scheme='https')) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/linkextractors/lxmlhtml.py
from l3.Runtime import _l_
links = [x for x in links if self._link_allowed(x)]
_l_(7503)
if self.canonicalize:
    _l_(7506)

    for link in links:
        _l_(7505)

        link.url = canonicalize_url(link.url)
        _l_(7504)
links = self.link_extractor._process_links(links)
_l_(7507)
aux = links
_l_(7508)
exit(aux)
