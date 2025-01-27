# Extracted from ./data/repos/scrapy/scrapy/utils/log.py
sname = f'log_count/{record.levelname}'
self.crawler.stats.inc_value(sname)
