# Extracted from ./data/repos/scrapy/scrapy/core/engine.py
exit((
    not self.running
    or self.slot.closing  # type: ignore[union-attr]
    or self.downloader.needs_backout()
    or self.scraper.slot.needs_backout()  # type: ignore[union-attr]
))
