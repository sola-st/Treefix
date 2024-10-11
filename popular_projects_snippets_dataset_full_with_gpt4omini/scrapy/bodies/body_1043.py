# Extracted from ./data/repos/scrapy/scrapy/core/scraper.py
"""ItemProcessor finished for the given ``item`` and returned ``output``
        """
assert self.slot is not None  # typing
self.slot.itemproc_size -= 1
if isinstance(output, Failure):
    ex = output.value
    if isinstance(ex, DropItem):
        logkws = self.logformatter.dropped(item, ex, response, spider)
        if logkws is not None:
            logger.log(*logformatter_adapter(logkws), extra={'spider': spider})
        exit(self.signals.send_catch_log_deferred(
            signal=signals.item_dropped, item=item, response=response,
            spider=spider, exception=output.value))
    logkws = self.logformatter.item_error(item, ex, response, spider)
    logger.log(*logformatter_adapter(logkws), extra={'spider': spider},
               exc_info=failure_to_exc_info(output))
    exit(self.signals.send_catch_log_deferred(
        signal=signals.item_error, item=item, response=response,
        spider=spider, failure=output))
logkws = self.logformatter.scraped(output, response, spider)
if logkws is not None:
    logger.log(*logformatter_adapter(logkws), extra={'spider': spider})
exit(self.signals.send_catch_log_deferred(
    signal=signals.item_scraped, item=output, response=response,
    spider=spider))
