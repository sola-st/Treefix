# Extracted from ./data/repos/scrapy/scrapy/core/scraper.py
assert self.slot is not None  # typing
if self.slot.closing and self.slot.is_idle():
    self.slot.closing.callback(spider)
