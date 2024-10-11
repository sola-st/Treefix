# Extracted from ./data/repos/scrapy/scrapy/http/response/text.py
"""
        A generator that produces :class:`~.Request` instances to follow all
        links in ``urls``. It accepts the same arguments as the :class:`~.Request`'s
        ``__init__`` method, except that each ``urls`` element does not need to be
        an absolute URL, it can be any of the following:

        * a relative URL
        * a :class:`~scrapy.link.Link` object, e.g. the result of
          :ref:`topics-link-extractors`
        * a :class:`~scrapy.selector.Selector` object for a ``<link>`` or ``<a>`` element, e.g.
          ``response.css('a.my_link')[0]``
        * an attribute :class:`~scrapy.selector.Selector` (not SelectorList), e.g.
          ``response.css('a::attr(href)')[0]`` or
          ``response.xpath('//img/@src')[0]``

        In addition, ``css`` and ``xpath`` arguments are accepted to perform the link extraction
        within the ``follow_all`` method (only one of ``urls``, ``css`` and ``xpath`` is accepted).

        Note that when passing a ``SelectorList`` as argument for the ``urls`` parameter or
        using the ``css`` or ``xpath`` parameters, this method will not produce requests for
        selectors from which links cannot be obtained (for instance, anchor tags without an
        ``href`` attribute)
        """
arguments = [x for x in (urls, css, xpath) if x is not None]
if len(arguments) != 1:
    raise ValueError(
        "Please supply exactly one of the following arguments: urls, css, xpath"
    )
if not urls:
    if css:
        urls = self.css(css)
    if xpath:
        urls = self.xpath(xpath)
if isinstance(urls, parsel.SelectorList):
    selectors = urls
    urls = []
    for sel in selectors:
        with suppress(_InvalidSelector):
            urls.append(_url_from_selector(sel))
exit(super().follow_all(
    urls=urls,
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
))
