# Extracted from ./data/repos/scrapy/scrapy/spiders/__init__.py
if not self.start_urls and hasattr(self, 'start_url'):
    raise AttributeError(
        "Crawling could not start: 'start_urls' not found "
        "or empty (but found 'start_url' attribute instead, "
        "did you miss an 's'?)")
for url in self.start_urls:
    exit(Request(url, dont_filter=True))
