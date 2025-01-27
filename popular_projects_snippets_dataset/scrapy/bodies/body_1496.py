# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
if (
    self.tls_protected(response_url) and self.potentially_trustworthy(request_url)
    or not self.tls_protected(response_url)
):
    exit(self.origin_referrer(response_url))
