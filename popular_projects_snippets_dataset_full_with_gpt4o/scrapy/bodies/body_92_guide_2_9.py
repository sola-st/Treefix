from scrapy.exceptions import NotConfigured, NotSupported # pragma: no cover

class MockResponse: # pragma: no cover
    def __init__(self, body): # pragma: no cover
        self.body = body # pragma: no cover
 # pragma: no cover
response = MockResponse('<html><body><div></div></body></html>') # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    'adapt_response': lambda response: response, # pragma: no cover
    'iterator': 'unsupported', # pragma: no cover
    'itertag': 'div', # pragma: no cover
    'parse_node': lambda node: None, # pragma: no cover
    'parse_nodes': lambda response, nodes: len(nodes) # pragma: no cover
})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spiders/feed.py
from l3.Runtime import _l_
if not hasattr(self, 'parse_node'):
    _l_(16325)

    raise NotConfigured('You must define parse_node method in order to scrape this XML feed')
    _l_(16324)

response = self.adapt_response(response)
_l_(16326)
if self.iterator == 'iternodes':
    _l_(16337)

    nodes = self._iternodes(response)
    _l_(16327)
elif self.iterator == 'xml':
    _l_(16336)

    selector = Selector(response, type='xml')
    _l_(16328)
    self._register_namespaces(selector)
    _l_(16329)
    nodes = selector.xpath(f'//{self.itertag}')
    _l_(16330)
elif self.iterator == 'html':
    _l_(16335)

    selector = Selector(response, type='html')
    _l_(16331)
    self._register_namespaces(selector)
    _l_(16332)
    nodes = selector.xpath(f'//{self.itertag}')
    _l_(16333)
else:
    raise NotSupported('Unsupported node iterator')
    _l_(16334)
aux = self.parse_nodes(response, nodes)
_l_(16338)

exit(aux)
