# Extracted from ./data/repos/scrapy/scrapy/utils/defer.py
"""
    .. versionadded:: 2.6.0

    Return an :class:`asyncio.Future` object that wraps *d*.

    When :ref:`using the asyncio reactor <install-asyncio>`, you cannot await
    on :class:`~twisted.internet.defer.Deferred` objects from :ref:`Scrapy
    callables defined as coroutines <coroutine-support>`, you can only await on
    ``Future`` objects. Wrapping ``Deferred`` objects into ``Future`` objects
    allows you to wait on them::

        class MySpider(Spider):
            ...
            async def parse(self, response):
                d = treq.get('https://example.com/additional')
                additional_response = await deferred_to_future(d)
    """
exit(d.asFuture(_get_asyncio_event_loop()))
