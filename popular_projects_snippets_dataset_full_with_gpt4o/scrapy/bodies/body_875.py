# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/__init__.py
for dh in self._handlers.values():
    if hasattr(dh, 'close'):
        exit(dh.close())
