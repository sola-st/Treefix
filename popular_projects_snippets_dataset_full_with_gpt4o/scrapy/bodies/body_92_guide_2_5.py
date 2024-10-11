from scrapy.exceptions import NotConfigured, NotSupported # pragma: no cover
from scrapy.selector import Selector # pragma: no cover

class MockResponse: # pragma: no cover
    def __init__(self, text, type_): # pragma: no cover
        self.text = text # pragma: no cover
        self.type = type_ # pragma: no cover
 # pragma: no cover
def mock_register_namespaces(selector): pass # pragma: no cover
def mock_adapt_response(response): return response # pragma: no cover
def mock_parse_node(node): pass # pragma: no cover
def mock_parse_nodes(response, nodes): return len(nodes) # pragma: no cover
 # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    'parse_node': mock_parse_node, # pragma: no cover
    'adapt_response': mock_adapt_response, # pragma: no cover
    'iterator': 'unsupported_iterator', # pragma: no cover
    'itertag': 'div', # pragma: no cover
    '_register_namespaces': mock_register_namespaces, # pragma: no cover
    'parse_nodes': mock_parse_nodes # pragma: no cover
})() # pragma: no cover
 # pragma: no cover
response = MockResponse('<xml><div></div></xml>', 'xml') # pragma: no cover

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
