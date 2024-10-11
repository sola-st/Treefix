from lxml import etree # pragma: no cover
from scrapy import Selector # pragma: no cover
from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy.exceptions import NotSupported # pragma: no cover

response = type('MockResponse', (object,), {'body': '<xml></xml>'})() # pragma: no cover
self = type('Mock', (object,), {'adapt_response': lambda self, resp: resp, 'iterator': 'xml', '_iternodes': lambda self, response: [], '_register_namespaces': lambda self, selector: None, 'itertag': 'item', 'parse_nodes': lambda self, response, nodes: None})() # pragma: no cover

from lxml import etree # pragma: no cover
from scrapy import Selector # pragma: no cover
from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy.exceptions import NotSupported # pragma: no cover

def parse_node(*args, **kwargs): pass # pragma: no cover
response = type('MockResponse', (object,), {'body': '<xml></xml>'})() # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    'adapt_response': lambda self, resp: resp, # pragma: no cover
    'iterator': 'xml', # pragma: no cover
    '_iternodes': lambda self, response: [], # pragma: no cover
    '_register_namespaces': lambda self, selector: None, # pragma: no cover
    'itertag': 'item', # pragma: no cover
    'parse_nodes': lambda self, response, nodes: None, # pragma: no cover
    'parse_node': parse_node # pragma: no cover
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
