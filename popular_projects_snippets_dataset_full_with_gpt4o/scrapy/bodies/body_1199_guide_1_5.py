import parsel # pragma: no cover
import scrapy # pragma: no cover

url = parsel.SelectorList([parsel.Selector('<a href="example.com">Example</a>')]) # pragma: no cover
callback = lambda response: response # pragma: no cover
method = 'GET' # pragma: no cover
headers = {'User-Agent': 'test-agent'} # pragma: no cover
body = None # pragma: no cover
cookies = None # pragma: no cover
meta = {} # pragma: no cover
encoding = None # pragma: no cover
priority = 0 # pragma: no cover
dont_filter = False # pragma: no cover
errback = None # pragma: no cover
cb_kwargs = {} # pragma: no cover
flags = None # pragma: no cover
self = type('Mock', (scrapy.http.Response,), {'encoding': 'utf-8', 'follow': lambda *args, **kwargs: 'Follow initiated'}) # pragma: no cover
class MockSuperFollow: # pragma: no cover
    def follow(self, url, callback=None, method='GET', headers=None, body=None, cookies=None, meta=None, encoding='utf-8', priority=0, dont_filter=False, errback=None, cb_kwargs=None, flags=None): # pragma: no cover
        return 'Following URL with given parameters' # pragma: no cover
super = MockSuperFollow() # pragma: no cover

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
