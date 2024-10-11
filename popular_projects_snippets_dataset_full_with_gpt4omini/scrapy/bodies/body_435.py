# Extracted from ./data/repos/scrapy/scrapy/utils/defer.py
"""
    .. versionadded:: 2.6.0

    Return *d* as an object that can be awaited from a :ref:`Scrapy callable
    defined as a coroutine <coroutine-support>`.

    What you can await in Scrapy callables defined as coroutines depends on the
    value of :setting:`TWISTED_REACTOR`:

    -   When not using the asyncio reactor, you can only await on
        :class:`~twisted.internet.defer.Deferred` objects.

    -   When :ref:`using the asyncio reactor <install-asyncio>`, you can only
        await on :class:`asyncio.Future` objects.

    If you want to write code that uses ``Deferred`` objects but works with any
    reactor, use this function on all ``Deferred`` objects::

        class MySpider(Spider):
            ...
            async def parse(self, response):
                d = treq.get('https://example.com/additional')
                extra_response = await maybe_deferred_to_future(d)
    """
if not is_asyncio_reactor_installed():
    exit(d)
exit(deferred_to_future(d))
