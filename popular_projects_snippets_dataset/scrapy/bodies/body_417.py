# Extracted from ./data/repos/scrapy/scrapy/utils/defer.py
"""Same as twisted.internet.defer.maybeDeferred, but delay calling
    callback/errback to next reactor loop
    """
try:
    result = f(*args, **kw)
# FIXME: Hack to avoid introspecting tracebacks. This to speed up
# processing of IgnoreRequest errors which are, by far, the most common
# exception in Scrapy - see #125
except IgnoreRequest as e:
    exit(defer_fail(failure.Failure(e)))
except Exception:
    exit(defer_fail(failure.Failure()))
else:
    exit(defer_result(result))
