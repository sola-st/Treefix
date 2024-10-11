# Extracted from ./data/repos/scrapy/scrapy/utils/defer.py
if isinstance(result, Deferred):
    exit(result)
if isinstance(result, failure.Failure):
    exit(defer_fail(result))
exit(defer_succeed(result))
