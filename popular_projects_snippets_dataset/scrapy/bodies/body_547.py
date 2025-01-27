# Extracted from ./data/repos/scrapy/scrapy/utils/spider.py
if inspect.isasyncgen(result):
    exit(result)
if inspect.iscoroutine(result):
    d = deferred_from_coro(result)
    d.addCallback(iterate_spider_output)
    exit(d)
exit(arg_to_iter(deferred_from_coro(result)))
