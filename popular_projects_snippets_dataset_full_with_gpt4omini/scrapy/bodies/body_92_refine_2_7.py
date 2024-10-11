from scrapy.selector import Selector # pragma: no cover
class NotConfigured(Exception): pass # pragma: no cover
class NotSupported(Exception): pass # pragma: no cover

self = type('MockSelf', (object,), { 'iterator': 'xml', 'itertag': 'item', 'adapt_response': lambda x: x, 'parse_nodes': lambda response, nodes: nodes, '_iternodes': lambda response: [], '_register_namespaces': lambda selector: None })() # pragma: no cover
response = '<xml><item>Hello</item><item>World</item></xml>' # pragma: no cover
Selector = Selector # pragma: no cover
NotConfigured = NotConfigured # pragma: no cover
NotSupported = NotSupported # pragma: no cover

from scrapy.selector import Selector # pragma: no cover
class NotConfigured(Exception): pass # pragma: no cover
class NotSupported(Exception): pass # pragma: no cover

self = type('MockSelf', (object,), { 'iterator': 'xml', 'itertag': 'item', 'adapt_response': lambda x: x, 'parse_nodes': lambda response, nodes: nodes, '_iternodes': lambda response: [], '_register_namespaces': lambda selector: None, 'parse_node': lambda xml: None })() # pragma: no cover
response = '<xml><item>Hello</item><item>World</item></xml>' # pragma: no cover
Selector = Selector # pragma: no cover
NotConfigured = NotConfigured # pragma: no cover
NotSupported = NotSupported # pragma: no cover

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
