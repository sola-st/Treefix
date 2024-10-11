import parsel # pragma: no cover
import scrapy # pragma: no cover
from scrapy.http import Request # pragma: no cover

url = 'http://example.com' # pragma: no cover
class MockSelector: # pragma: no cover
    def __init__(self, text): # pragma: no cover
        self.text = text # pragma: no cover
    def get(self): # pragma: no cover
        return self.text # pragma: no cover
parsel.Selector = MockSelector # pragma: no cover
parsel.SelectorList = list # pragma: no cover
def _url_from_selector(selector): # pragma: no cover
    return selector.get() # pragma: no cover
class MockSelf: # pragma: no cover
    encoding = 'utf-8' # pragma: no cover
self = MockSelf() # pragma: no cover
encoding = None # pragma: no cover
callback = lambda response: None # pragma: no cover
method = 'GET' # pragma: no cover
headers = {'User-Agent': 'Mozilla/5.0'} # pragma: no cover
body = None # pragma: no cover
cookies = {'sessionid': '12345'} # pragma: no cover
meta = {'key': 'value'} # pragma: no cover
priority = 0 # pragma: no cover
dont_filter = False # pragma: no cover
errback = lambda failure: None # pragma: no cover
cb_kwargs = {} # pragma: no cover
flags = [] # pragma: no cover

import parsel # pragma: no cover
from scrapy.http import Request # pragma: no cover
from scrapy import Spider # pragma: no cover

url = 'http://example.com' # pragma: no cover
parsel.Selector = type('MockSelector', (object,), {'get': lambda self: 'http://example.com'}) # pragma: no cover
parsel.SelectorList = type('MockSelectorList', (object,), {}) # pragma: no cover
_url_from_selector = lambda selector: 'http://example.com/from_selector' # pragma: no cover
class MockSpider(Spider): # pragma: no cover
    encoding = 'utf-8' # pragma: no cover
    def follow(self, url, callback=None, method='GET', headers=None, body=None, cookies=None, meta=None, encoding=None, priority=0, dont_filter=False, errback=None, cb_kwargs=None, flags=None): # pragma: no cover
        return Request(url, callback=callback, method=method, headers=headers, body=body, cookies=cookies, meta=meta, encoding=encoding, priority=priority, dont_filter=dont_filter, errback=errback, cb_kwargs=cb_kwargs, flags=flags) # pragma: no cover
encoding = None # pragma: no cover
callback = lambda response: None # pragma: no cover
method = 'GET' # pragma: no cover
headers = {'User-Agent': 'Mozilla/5.0'} # pragma: no cover
body = None # pragma: no cover
cookies = {'sessionid': '12345'} # pragma: no cover
meta = {'key': 'value'} # pragma: no cover
priority = 0 # pragma: no cover
dont_filter = False # pragma: no cover
errback = lambda failure: None # pragma: no cover
cb_kwargs = {} # pragma: no cover
flags = [] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/response/text.py
from l3.Runtime import _l_
"""
        Return a :class:`~.Request` instance to follow a link ``url``.
        It accepts the same arguments as ``Request.__init__`` method,
        but ``url`` can be not only an absolute URL, but also

        * a relative URL
        * a :class:`~scrapy.link.Link` object, e.g. the result of
          :ref:`topics-link-extractors`
        * a :class:`~scrapy.selector.Selector` object for a ``<link>`` or ``<a>`` element, e.g.
          ``response.css('a.my_link')[0]``
        * an attribute :class:`~scrapy.selector.Selector` (not SelectorList), e.g.
          ``response.css('a::attr(href)')[0]`` or
          ``response.xpath('//img/@src')[0]``

        See :ref:`response-follow-example` for usage examples.
        """
if isinstance(url, parsel.Selector):
    _l_(20295)

    url = _url_from_selector(url)
    _l_(20292)
elif isinstance(url, parsel.SelectorList):
    _l_(20294)

    raise ValueError("SelectorList is not supported")
    _l_(20293)
encoding = self.encoding if encoding is None else encoding
_l_(20296)
aux = super().follow(
    url=url,
    callback=callback,
    method=method,
    headers=headers,
    body=body,
    cookies=cookies,
    meta=meta,
    encoding=encoding,
    priority=priority,
    dont_filter=dont_filter,
    errback=errback,
    cb_kwargs=cb_kwargs,
    flags=flags,
)
_l_(20297)
exit(aux)
