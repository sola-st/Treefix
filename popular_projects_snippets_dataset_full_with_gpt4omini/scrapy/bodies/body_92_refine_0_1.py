from lxml import etree # pragma: no cover
from scrapy.selector import Selector # pragma: no cover
from scrapy.exceptions import NotConfigured, NotSupported # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
self.parse_node = lambda xml: etree.fromstring(xml) # pragma: no cover
response = '<root><item>Test</item></root>' # pragma: no cover
Selector = lambda response, type: type == 'xml' and etree.XML(response) or etree.HTML(response) # pragma: no cover
NotConfigured = Exception('Configuration Error') # pragma: no cover
NotSupported = Exception('Not Supported Error') # pragma: no cover
self.adapt_response = lambda response: response # pragma: no cover
self.iterator = 'xml' # pragma: no cover
self._iternodes = lambda response: [response] # pragma: no cover
self._register_namespaces = lambda selector: None # pragma: no cover
self.itertag = 'item' # pragma: no cover
self.parse_nodes = lambda response, nodes: 'Parsed Nodes' # pragma: no cover

from lxml import etree # pragma: no cover
from scrapy.selector import Selector # pragma: no cover
from scrapy.exceptions import NotConfigured, NotSupported # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
self.parse_node = lambda xml: etree.fromstring(xml) # pragma: no cover
response = '<root><item>Test</item></root>' # pragma: no cover
class MockSelector:  # Mocking the Selector behavior with a class # pragma: no cover
    def __init__(self, response, type): # pragma: no cover
        self.response = response # pragma: no cover
        self.type = type # pragma: no cover
    def xpath(self, query): # pragma: no cover
        if self.type == 'xml': # pragma: no cover
            return [etree.fromstring(self.response)] if query == '//item' else [] # pragma: no cover
        elif self.type == 'html': # pragma: no cover
            return [etree.HTML(self.response)] if query == '//item' else [] # pragma: no cover
        return [] # pragma: no cover
Selector = MockSelector # pragma: no cover
NotConfigured = Exception('Configuration Error') # pragma: no cover
NotSupported = Exception('Not Supported Error') # pragma: no cover
self.adapt_response = lambda response: response # pragma: no cover
self.iterator = 'xml' # pragma: no cover
self._iternodes = lambda response: [response] # pragma: no cover
self._register_namespaces = lambda selector: None # pragma: no cover
self.itertag = 'item' # pragma: no cover
self.parse_nodes = lambda response, nodes: 'Parsed Nodes' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spiders/feed.py
from l3.Runtime import _l_
if not hasattr(self, 'parse_node'):
    _l_(4707)

    raise NotConfigured('You must define parse_node method in order to scrape this XML feed')
    _l_(4706)

response = self.adapt_response(response)
_l_(4708)
if self.iterator == 'iternodes':
    _l_(4719)

    nodes = self._iternodes(response)
    _l_(4709)
elif self.iterator == 'xml':
    _l_(4718)

    selector = Selector(response, type='xml')
    _l_(4710)
    self._register_namespaces(selector)
    _l_(4711)
    nodes = selector.xpath(f'//{self.itertag}')
    _l_(4712)
elif self.iterator == 'html':
    _l_(4717)

    selector = Selector(response, type='html')
    _l_(4713)
    self._register_namespaces(selector)
    _l_(4714)
    nodes = selector.xpath(f'//{self.itertag}')
    _l_(4715)
else:
    raise NotSupported('Unsupported node iterator')
    _l_(4716)
aux = self.parse_nodes(response, nodes)
_l_(4720)

exit(aux)
