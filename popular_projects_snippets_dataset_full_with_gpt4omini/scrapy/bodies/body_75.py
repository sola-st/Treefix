# Extracted from ./data/repos/scrapy/scrapy/spiders/crawl.py
self.callback = _get_method(self.callback, spider)
self.errback = _get_method(self.errback, spider)
self.process_links = _get_method(self.process_links, spider)
self.process_request = _get_method(self.process_request, spider)
