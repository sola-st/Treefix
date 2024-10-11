# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
if not self.tls_protected(response_url) or self.tls_protected(request_url):
    exit(self.stripped_referrer(response_url))
