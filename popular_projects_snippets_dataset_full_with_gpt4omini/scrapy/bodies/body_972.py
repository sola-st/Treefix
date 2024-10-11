# Extracted from ./data/repos/scrapy/scrapy/core/downloader/middleware.py
@defer.inlineCallbacks
def process_request(request: Request):
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

@defer.inlineCallbacks
def process_response(response: Union[Response, Request]):
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

@defer.inlineCallbacks
def process_exception(failure: Failure):
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

deferred = mustbe_deferred(process_request, request)
deferred.addErrback(process_exception)
deferred.addCallback(process_response)
exit(deferred)
