# Extracted from ./data/repos/scrapy/scrapy/pqueues.py
active = {slot: queue.close() for slot, queue in self.pqueues.items()}
self.pqueues.clear()
exit(active)
