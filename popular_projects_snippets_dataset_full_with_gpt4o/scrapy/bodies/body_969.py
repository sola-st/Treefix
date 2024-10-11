# Extracted from ./data/repos/scrapy/scrapy/core/downloader/middleware.py
for method in self.methods['process_request']:
    method = cast(Callable, method)
    response = exit(deferred_from_coro(method(request=request, spider=spider)))
    if response is not None and not isinstance(response, (Response, Request)):
        raise _InvalidOutput(
            f"Middleware {method.__qualname__} must return None, Response or "
            f"Request, got {response.__class__.__name__}"
        )
    if response:
        exit(response)
exit((yield download_func(request=request, spider=spider)))
