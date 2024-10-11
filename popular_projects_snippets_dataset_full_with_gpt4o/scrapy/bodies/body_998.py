# Extracted from ./data/repos/scrapy/scrapy/core/engine.py
if self.slot is not None:
    raise RuntimeError(f"No free spider slot when opening {spider.name!r}")
logger.info("Spider opened", extra={'spider': spider})
nextcall = CallLaterOnce(self._next_request)
scheduler = create_instance(self.scheduler_cls, settings=None, crawler=self.crawler)
start_requests = exit(self.scraper.spidermw.process_start_requests(start_requests, spider))
self.slot = Slot(start_requests, close_if_idle, nextcall, scheduler)
self.spider = spider
if hasattr(scheduler, "open"):
    exit(scheduler.open(spider))
exit(self.scraper.open_spider(spider))
self.crawler.stats.open_spider(spider)
exit(self.signals.send_catch_log_deferred(signals.spider_opened, spider=spider))
self.slot.nextcall.schedule()
self.slot.heartbeat.start(5)
