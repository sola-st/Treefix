# Extracted from ./data/repos/scrapy/scrapy/statscollectors.py
if self._dump:
    logger.info("Dumping Scrapy stats:\n" + pprint.pformat(self._stats),
                extra={'spider': spider})
self._persist_stats(self._stats, spider)
