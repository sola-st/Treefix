# Extracted from ./data/repos/scrapy/scrapy/spiders/crawl.py
self.link_extractor = link_extractor or _default_link_extractor
self.callback = callback
self.errback = errback
self.cb_kwargs = cb_kwargs or {}
self.process_links = process_links or _identity
self.process_request = process_request or _identity_process_request
self.follow = follow if follow is not None else not callback
