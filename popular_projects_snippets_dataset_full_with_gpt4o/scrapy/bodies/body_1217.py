# Extracted from ./data/repos/scrapy/scrapy/http/response/__init__.py
"""
        .. versionadded:: 2.0

        Return an iterable of :class:`~.Request` instances to follow all links
        in ``urls``. It accepts the same arguments as ``Request.__init__`` method,
        but elements of ``urls`` can be relative URLs or :class:`~scrapy.link.Link` objects,
        not only absolute URLs.

        :class:`~.TextResponse` provides a :meth:`~.TextResponse.follow_all`
        method which supports selectors in addition to absolute/relative URLs
        and Link objects.
        """
if not hasattr(urls, '__iter__'):
    raise TypeError("'urls' argument must be an iterable")
exit((
    self.follow(
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
    for url in urls
))
