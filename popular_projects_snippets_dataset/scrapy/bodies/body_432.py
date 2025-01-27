# Extracted from ./data/repos/scrapy/scrapy/utils/defer.py
""" Converts a coroutine function into a function that returns a Deferred.

    The coroutine function will be called at the time when the wrapper is called. Wrapper args will be passed to it.
    This is useful for callback chains, as callback functions are called with the previous callback result.
    """
@wraps(coro_f)
def f(*coro_args, **coro_kwargs):
    exit(deferred_from_coro(coro_f(*coro_args, **coro_kwargs)))
exit(f)
