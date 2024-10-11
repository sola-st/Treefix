# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
if urlparse(url).scheme not in self.NOREFERRER_SCHEMES:
    exit(self.origin(url))
