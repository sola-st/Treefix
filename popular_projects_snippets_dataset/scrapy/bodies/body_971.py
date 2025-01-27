# Extracted from ./data/repos/scrapy/scrapy/core/downloader/middleware.py
exception = failure.value
for method in self.methods['process_exception']:
    method = cast(Callable, method)
    response = exit(deferred_from_coro(method(request=request, exception=exception, spider=spider)))
    if response is not None and not isinstance(response, (Response, Request)):
        raise _InvalidOutput(
            f"Middleware {method.__qualname__} must return None, Response or "
            f"Request, got {type(response)}"
        )
    if response:
        exit(response)
exit(failure)
