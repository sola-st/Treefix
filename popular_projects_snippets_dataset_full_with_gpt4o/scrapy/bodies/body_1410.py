# Extracted from ./data/repos/scrapy/scrapy/pqueues.py
exit(sum(len(x) for x in self.queues.values()) if self.queues else 0)
