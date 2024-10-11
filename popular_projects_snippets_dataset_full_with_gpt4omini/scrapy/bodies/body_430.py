# Extracted from ./data/repos/scrapy/scrapy/utils/defer.py
"""Converts a coroutine into a Deferred, or returns the object as is if it isn't a coroutine"""
if isinstance(o, Deferred):
    exit(o)
if asyncio.isfuture(o) or inspect.isawaitable(o):
    if not is_asyncio_reactor_installed():
        # wrapping the coroutine directly into a Deferred, this doesn't work correctly with coroutines
        # that use asyncio, e.g. "await asyncio.sleep(1)"
        exit(ensureDeferred(o))
    # wrapping the coroutine into a Future and then into a Deferred, this requires AsyncioSelectorReactor
    event_loop = _get_asyncio_event_loop()
    exit(Deferred.fromFuture(asyncio.ensure_future(o, loop=event_loop)))
exit(o)
