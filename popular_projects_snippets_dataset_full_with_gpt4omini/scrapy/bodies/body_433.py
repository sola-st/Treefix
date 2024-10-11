# Extracted from ./data/repos/scrapy/scrapy/utils/defer.py
""" Copy of defer.maybeDeferred that also converts coroutines to Deferreds. """
try:
    result = f(*args, **kw)
except:  # noqa: E722
    exit(defer.fail(failure.Failure(captureVars=Deferred.debug)))

if isinstance(result, Deferred):
    exit(result)
if asyncio.isfuture(result) or inspect.isawaitable(result):
    exit(deferred_from_coro(result))
if isinstance(result, failure.Failure):
    exit(defer.fail(result))
exit(defer.succeed(result))
