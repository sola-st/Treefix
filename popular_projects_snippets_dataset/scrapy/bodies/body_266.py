# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
logger.info(
    "Stored %s", logmsg,
    extra={'spider': spider}
)
self.crawler.stats.inc_value(f"feedexport/success_count/{slot_type}")
