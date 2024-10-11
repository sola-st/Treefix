# Extracted from ./data/repos/scrapy/scrapy/extensions/corestats.py
self.start_time = datetime.utcnow()
self.stats.set_value('start_time', self.start_time, spider=spider)
