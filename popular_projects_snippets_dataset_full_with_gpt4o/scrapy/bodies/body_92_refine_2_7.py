from scrapy.selector import Selector # pragma: no cover
import sys # pragma: no cover

self = type('Mock', (object,), {'adapt_response': lambda self, response: response, 'iterator': 'xml', '_iternodes': lambda self, response: [], '_register_namespaces': lambda self, selector: None, 'itertag': 'item', 'parse_nodes': lambda self, response, nodes: 0})() # pragma: no cover
class NotConfigured(Exception): pass # pragma: no cover
response = '''<root></root>''' # pragma: no cover
class NotSupported(Exception): pass # pragma: no cover

from scrapy.selector import Selector # pragma: no cover
from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy.exceptions import NotSupported # pragma: no cover

class MockScraper: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.iterator = 'xml' # pragma: no cover
        self.itertag = 'item' # pragma: no cover
     # pragma: no cover
    def adapt_response(self, response): # pragma: no cover
        return response # pragma: no cover
     # pragma: no cover
    def _iternodes(self, response): # pragma: no cover
        return ['<node>Node1</node>', '<node>Node2</node>'] # pragma: no cover
     # pragma: no cover
    def _register_namespaces(self, selector): # pragma: no cover
        pass # pragma: no cover
     # pragma: no cover
    def parse_nodes(self, response, nodes): # pragma: no cover
        # Dummy parse_nodes method implementation # pragma: no cover
        return 0 # pragma: no cover
     # pragma: no cover
    def parse_node(self):  # Dummy parse_node method to avoid NotConfigured error # pragma: no cover
        pass # pragma: no cover
     # pragma: no cover
self = MockScraper() # pragma: no cover
response = type('MockResponse', (object,), {'body': '<root><item>Item 1</item><item>Item 2</item></root>'})() # pragma: no cover

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
