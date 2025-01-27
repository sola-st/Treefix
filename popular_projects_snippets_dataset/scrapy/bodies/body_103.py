# Extracted from ./data/repos/scrapy/scrapy/shell.py
if self.spider:
    exit(self.spider)

if spider is None:
    spider = self.crawler.spider or self.crawler._create_spider()

self.crawler.spider = spider
self.crawler.engine.open_spider(spider, close_if_idle=False)
self.spider = spider
exit(spider)
