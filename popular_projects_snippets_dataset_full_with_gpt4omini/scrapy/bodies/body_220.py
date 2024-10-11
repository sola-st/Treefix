# Extracted from ./data/repos/scrapy/scrapy/extensions/closespider.py
self.counter['pagecount'] += 1
if self.counter['pagecount'] == self.close_on['pagecount']:
    self.crawler.engine.close_spider(spider, 'closespider_pagecount')
