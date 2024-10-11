import parsel # pragma: no cover
from scrapy import Request # pragma: no cover

url = 'http://example.com' # pragma: no cover
parsel = type('MockParsel', (object,), {'Selector': type('Selector', (object,), {}), 'SelectorList': type('SelectorList', (object,), {})}) # pragma: no cover
_url_from_selector = lambda selector: 'http://example.com/from_selector' # pragma: no cover
self = type('MockSelf', (object,), {'encoding': 'utf-8'})() # pragma: no cover
encoding = None # pragma: no cover
callback = lambda response: None # pragma: no cover
method = 'GET' # pragma: no cover
headers = {'User-Agent': 'Mozilla/5.0'} # pragma: no cover
body = None # pragma: no cover
cookies = {'session': 'abc123'} # pragma: no cover
meta = {'download_timeout': 15} # pragma: no cover
priority = 0 # pragma: no cover
dont_filter = True # pragma: no cover
errback = lambda failure: None # pragma: no cover
cb_kwargs = {'param1': 'value1'} # pragma: no cover
flags = ['flag1', 'flag2'] # pragma: no cover

import parsel # pragma: no cover
from scrapy.http import HtmlResponse # pragma: no cover

url = 'http://example.com' # pragma: no cover
parsel = type('MockParsel', (object,), {'Selector': type('Selector', (object,), {}), 'SelectorList': type('SelectorList', (object,), {})})() # pragma: no cover
_url_from_selector = lambda selector: 'http://example.com/from_selector' # pragma: no cover
self = type('MockSelf', (object,), {'encoding': 'utf-8', 'follow': lambda self, url, callback, method, headers, body, cookies, meta, encoding, priority, dont_filter, errback, cb_kwargs, flags: 'Following URL'})() # pragma: no cover
encoding = None # pragma: no cover
callback = lambda response: None # pragma: no cover
method = 'GET' # pragma: no cover
headers = {'User-Agent': 'Mozilla/5.0'} # pragma: no cover
body = None # pragma: no cover
cookies = {'session': 'abc123'} # pragma: no cover
meta = {'download_timeout': 15} # pragma: no cover
priority = 0 # pragma: no cover
dont_filter = True # pragma: no cover
errback = lambda failure: None # pragma: no cover
cb_kwargs = {'param1': 'value1'} # pragma: no cover
flags = ['flag1', 'flag2'] # pragma: no cover

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
