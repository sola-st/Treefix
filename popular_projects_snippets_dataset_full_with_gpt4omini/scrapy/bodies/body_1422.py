# Extracted from ./data/repos/scrapy/scrapy/pqueues.py
exit(sum(len(x) for x in self.pqueues.values()) if self.pqueues else 0)
