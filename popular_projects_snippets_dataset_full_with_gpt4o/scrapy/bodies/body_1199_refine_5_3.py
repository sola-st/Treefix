from parsel import Selector, SelectorList # pragma: no cover

url = 'https://example.com' # pragma: no cover
parsel = type('Mock', (object,), {'Selector': Selector, 'SelectorList': SelectorList}) # pragma: no cover
_url_from_selector = lambda x: 'https://example.com/from_selector' # pragma: no cover
self = type('Mock', (object,), {'encoding': 'utf-8'})() # pragma: no cover
encoding = None # pragma: no cover
callback = lambda response: None # pragma: no cover
method = 'GET' # pragma: no cover
headers = {'User-Agent': 'Mozilla/5.0'} # pragma: no cover
body = None # pragma: no cover
cookies = {'sessionid': '12345'} # pragma: no cover
meta = {'download_timeout': 15} # pragma: no cover
priority = 0 # pragma: no cover
dont_filter = False # pragma: no cover
errback = lambda failure: None # pragma: no cover
cb_kwargs = {} # pragma: no cover
flags = ['example_flag'] # pragma: no cover

import parsel # pragma: no cover
from scrapy import Request # pragma: no cover
from scrapy.http import Response # pragma: no cover

url = 'http://example.com' # pragma: no cover
parsel.Selector = type('MockSelector', (object,), {}) # pragma: no cover
parsel.SelectorList = type('MockSelectorList', (object,), {}) # pragma: no cover
_url_from_selector = lambda x: 'http://example.com/from_selector' # pragma: no cover
self = type('MockSelf', (Request,), {'encoding': 'utf-8'})('http://example.com') # pragma: no cover
encoding = None # pragma: no cover
callback = None # pragma: no cover
method = 'GET' # pragma: no cover
headers = {'User-Agent': 'scrapy'} # pragma: no cover
body = b'' # pragma: no cover
cookies = {'session': 'abcd1234'} # pragma: no cover
meta = {'proxy': 'http://proxy.example.com'} # pragma: no cover
priority = 0 # pragma: no cover
dont_filter = False # pragma: no cover
errback = None # pragma: no cover
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
