from scrapy.selector import Selector # pragma: no cover

self = type('MockSelf', (object,), { # pragma: no cover
    'adapt_response': lambda self, response: response, # pragma: no cover
    'iterator': 'xml', # pragma: no cover
'_iternodes': lambda self, response: ['node1', 'node2'], # pragma: no cover
    '_register_namespaces': lambda self, selector: None, # pragma: no cover
    'itertag': 'item', # pragma: no cover
    'parse_nodes': lambda self, response, nodes: 0 # pragma: no cover
})() # pragma: no cover
class NotConfigured(Exception): pass # pragma: no cover
response = '<xml><item>Content</item></xml>' # pragma: no cover
class Selector: # pragma: no cover
    def __init__(self, response, type): # pragma: no cover
        self.type = type # pragma: no cover
        self.response = response # pragma: no cover
    def xpath(self, path): # pragma: no cover
        # A mock implementation of XPath # pragma: no cover
        return ['<item>Content</item>'] # pragma: no cover
class NotSupported(Exception): pass # pragma: no cover

from scrapy.selector import Selector # pragma: no cover
from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy.exceptions import NotSupported # pragma: no cover

class MockSelf: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.iterator = 'xml' # pragma: no cover
        self.itertag = 'item' # pragma: no cover
        self.parse_node = lambda: None # pragma: no cover
    def adapt_response(self, response): # pragma: no cover
        return response # pragma: no cover
    def _iternodes(self, response): # pragma: no cover
        return ['<item>Content</item>'] # pragma: no cover
    def _register_namespaces(self, selector): # pragma: no cover
        pass # pragma: no cover
    def parse_nodes(self, response, nodes): # pragma: no cover
        return 0 # pragma: no cover
self = MockSelf() # pragma: no cover
response = type('MockResponse', (object,), {'body': '<xml><item>Content</item></xml>'})() # pragma: no cover

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
