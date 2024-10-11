import parsel # pragma: no cover
from scrapy.http import Request # pragma: no cover

url = parsel.Selector('<a href="http://example.com">Example</a>') # pragma: no cover
encoding = None # pragma: no cover
self = type('Mock', (object,), {'encoding': 'utf-8', 'follow': lambda self, **kwargs: 'Followed'})() # pragma: no cover
callback = lambda response: None # pragma: no cover
method = 'GET' # pragma: no cover
headers = {'User-Agent': 'my-crawler'} # pragma: no cover
body = None # pragma: no cover
cookies = {} # pragma: no cover
meta = {} # pragma: no cover
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
    _l_(8808)

    url = _url_from_selector(url)
    _l_(8805)
elif isinstance(url, parsel.SelectorList):
    _l_(8807)

    raise ValueError("SelectorList is not supported")
    _l_(8806)
encoding = self.encoding if encoding is None else encoding
_l_(8809)
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
_l_(8810)
exit(aux)
