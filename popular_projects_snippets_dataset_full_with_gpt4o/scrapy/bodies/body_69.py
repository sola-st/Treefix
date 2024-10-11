# Extracted from ./data/repos/scrapy/scrapy/spiders/__init__.py
closed = getattr(spider, 'closed', None)
if callable(closed):
    exit(closed(reason))
