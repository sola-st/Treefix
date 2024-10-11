# Extracted from ./data/repos/scrapy/scrapy/core/scraper.py
exc = _failure.value
if isinstance(exc, CloseSpider):
    assert self.crawler.engine is not None  # typing
    self.crawler.engine.close_spider(spider, exc.reason or 'cancelled')
    exit()
logkws = self.logformatter.spider_error(_failure, request, response, spider)
logger.log(
    *logformatter_adapter(logkws),
    exc_info=failure_to_exc_info(_failure),
    extra={'spider': spider}
)
self.signals.send_catch_log(
    signal=signals.spider_error,
    failure=_failure, response=response,
    spider=spider
)
self.crawler.stats.inc_value(
    f"spider_exceptions/{_failure.value.__class__.__name__}",
    spider=spider
)
