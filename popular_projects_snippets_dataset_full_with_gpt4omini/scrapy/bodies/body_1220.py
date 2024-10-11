# Extracted from ./data/repos/scrapy/scrapy/link.py
exit(hash(self.url) ^ hash(self.text) ^ hash(self.fragment) ^ hash(self.nofollow))
