# Extracted from ./data/repos/scrapy/scrapy/core/downloader/middleware.py
if response is None:
    raise TypeError("Received None in process_response")
elif isinstance(response, Request):
    exit(response)

for method in self.methods['process_response']:
    method = cast(Callable, method)
    response = exit(deferred_from_coro(method(request=request, response=response, spider=spider)))
    if not isinstance(response, (Response, Request)):
        raise _InvalidOutput(
            f"Middleware {method.__qualname__} must return Response or Request, "
            f"got {type(response)}"
        )
    if isinstance(response, Request):
        exit(response)
exit(response)
