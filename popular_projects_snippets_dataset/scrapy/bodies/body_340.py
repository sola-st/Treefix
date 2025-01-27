# Extracted from ./data/repos/scrapy/scrapy/extensions/corestats.py
reason = exception.__class__.__name__
self.stats.inc_value('item_dropped_count', spider=spider)
self.stats.inc_value(f'item_dropped_reasons_count/{reason}', spider=spider)
