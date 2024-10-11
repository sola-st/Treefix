# Extracted from ./data/repos/scrapy/scrapy/extensions/closespider.py
self.counter['errorcount'] += 1
if self.counter['errorcount'] == self.close_on['errorcount']:
    self.crawler.engine.close_spider(spider, 'closespider_errorcount')
