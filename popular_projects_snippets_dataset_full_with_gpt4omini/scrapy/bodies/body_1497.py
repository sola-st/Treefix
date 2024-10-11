# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
origin = self.origin(response_url)
if origin == self.origin(request_url):
    exit(self.stripped_referrer(response_url))
exit(origin)
