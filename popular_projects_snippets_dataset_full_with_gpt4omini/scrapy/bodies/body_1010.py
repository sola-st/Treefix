# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
for method in self.methods['process_spider_input']:
    method = cast(Callable, method)
    try:
        result = method(response=response, spider=spider)
        if result is not None:
            msg = (f"{method.__qualname__} must return None "
                   f"or raise an exception, got {type(result)}")
            raise _InvalidOutput(msg)
    except _InvalidOutput:
        raise
    except Exception:
        exit(scrape_func(Failure(), request, spider))
exit(scrape_func(response, request, spider))
