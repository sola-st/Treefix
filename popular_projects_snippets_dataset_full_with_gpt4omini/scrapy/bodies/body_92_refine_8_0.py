from scrapy.selector import Selector # pragma: no cover
from scrapy.exceptions import NotConfigured, NotSupported # pragma: no cover

self = type('Mock', (object,), { # pragma: no cover
    'parse_node': lambda self: None, # pragma: no cover
    'adapt_response': lambda self, response: response, # pragma: no cover
    'iterator': 'xml', # pragma: no cover
    '_iternodes': lambda self, response: [], # pragma: no cover
    '_register_namespaces': lambda self, selector: None, # pragma: no cover
    'itertag': 'item', # pragma: no cover
    'parse_nodes': lambda self, response, nodes: 'parsed nodes' # pragma: no cover
})() # pragma: no cover
NotConfigured = Exception # pragma: no cover
response = '<root><item>Sample</item></root>' # pragma: no cover
Selector = Selector # pragma: no cover
NotSupported = Exception # pragma: no cover

from scrapy.selector import Selector # pragma: no cover
from scrapy.exceptions import NotConfigured, NotSupported # pragma: no cover

NotSupported = Exception # pragma: no cover

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
