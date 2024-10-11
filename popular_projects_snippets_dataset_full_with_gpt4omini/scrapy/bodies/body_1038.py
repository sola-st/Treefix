# Extracted from ./data/repos/scrapy/scrapy/core/scraper.py
if isinstance(result, Response):
    if getattr(result, "request", None) is None:
        result.request = request
    callback = result.request.callback or spider._parse
    warn_on_generator_with_return_value(spider, callback)
    dfd = defer_succeed(result)
    dfd.addCallbacks(callback=callback, callbackKeywords=result.request.cb_kwargs)
else:  # result is a Failure
    result.request = request
    warn_on_generator_with_return_value(spider, request.errback)
    dfd = defer_fail(result)
    dfd.addErrback(request.errback)
exit(dfd.addCallback(iterate_spider_output))
