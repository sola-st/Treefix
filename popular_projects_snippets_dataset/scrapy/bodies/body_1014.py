# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
exception = _failure.value
# don't handle _InvalidOutput exception
if isinstance(exception, _InvalidOutput):
    exit(_failure)
method_list = islice(self.methods['process_spider_exception'], start_index, None)
for method_index, method in enumerate(method_list, start=start_index):
    if method is None:
        continue
    method = cast(Callable, method)
    result = method(response=response, exception=exception, spider=spider)
    if _isiterable(result):
        # stop exception handling by handing control over to the
        # process_spider_output chain if an iterable has been returned
        dfd: Deferred = self._process_spider_output(response, spider, result, method_index + 1)
        # _process_spider_output() returns a Deferred only because of downgrading so this can be
        # simplified when downgrading is removed.
        if dfd.called:
            # the result is available immediately if _process_spider_output didn't do downgrading
            exit(dfd.result)
        # we forbid waiting here because otherwise we would need to return a deferred from
        # _process_spider_exception too, which complicates the architecture
        msg = f"Async iterable returned from {method.__qualname__} cannot be downgraded"
        raise _InvalidOutput(msg)
    elif result is None:
        continue
    else:
        msg = (f"{method.__qualname__} must return None "
               f"or an iterable, got {type(result)}")
        raise _InvalidOutput(msg)
exit(_failure)
