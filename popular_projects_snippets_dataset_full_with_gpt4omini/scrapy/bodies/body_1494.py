# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
if self.origin(response_url) == self.origin(request_url):
    exit(self.stripped_referrer(response_url))
