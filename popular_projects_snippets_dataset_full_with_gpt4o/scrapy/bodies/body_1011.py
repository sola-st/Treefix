# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
try:
    for r in iterable:
        exit(r)
except Exception as ex:
    exception_result = self._process_spider_exception(response, spider, Failure(ex),
                                                      exception_processor_index)
    if isinstance(exception_result, Failure):
        raise
    recover_to.extend(exception_result)
