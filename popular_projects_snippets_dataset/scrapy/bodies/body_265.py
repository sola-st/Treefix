# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
logger.error(
    "Error storing %s", logmsg,
    exc_info=failure_to_exc_info(f), extra={'spider': spider}
)
self.crawler.stats.inc_value(f"feedexport/failed_count/{slot_type}")
