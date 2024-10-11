import parsel # pragma: no cover
from scrapy.http import HtmlResponse # pragma: no cover
from scrapy.http import Request # pragma: no cover

class MockSuper: # pragma: no cover
    def follow(self, url, callback=None, method='GET', headers=None, body=None, cookies=None, meta=None, encoding='utf-8', priority=0, dont_filter=False, errback=None, cb_kwargs=None, flags=None): # pragma: no cover
        return 'Request created with url: {}'.format(url) # pragma: no cover
 # pragma: no cover
def _url_from_selector(selector): # pragma: no cover
    return selector.xpath('@href').get() # pragma: no cover
 # pragma: no cover
self = type('Mock', (MockSuper,), {'encoding': 'utf-8'})() # pragma: no cover
 # pragma: no cover
response = HtmlResponse( # pragma: no cover
    url='http://example.com', # pragma: no cover
    body='<html><body><a class="my_link" href="http://example.com">link</a></body></html>', # pragma: no cover
    encoding='utf-8' # pragma: no cover
) # pragma: no cover
url = response.css('a') # pragma: no cover
callback = None # pragma: no cover
method = 'GET' # pragma: no cover
headers = None # pragma: no cover
body = None # pragma: no cover
cookies = None # pragma: no cover
meta = None # pragma: no cover
encoding = None # pragma: no cover
priority = 0 # pragma: no cover
dont_filter = False # pragma: no cover
errback = None # pragma: no cover
cb_kwargs = {} # pragma: no cover
flags = None # pragma: no cover

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
