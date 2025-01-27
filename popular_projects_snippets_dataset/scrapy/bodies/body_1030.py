# Extracted from ./data/repos/scrapy/scrapy/core/scraper.py
"""Close a spider being scraped and release its resources"""
if self.slot is None:
    raise RuntimeError("Scraper slot not assigned")
self.slot.closing = Deferred()
self.slot.closing.addCallback(self.itemproc.close_spider)
self._check_if_closing(spider)
exit(self.slot.closing)
