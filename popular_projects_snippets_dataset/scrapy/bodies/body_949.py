# Extracted from ./data/repos/scrapy/scrapy/core/downloader/__init__.py
if self.latercall and self.latercall.active():
    self.latercall.cancel()
