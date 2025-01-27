# Extracted from ./data/repos/scrapy/scrapy/pqueues.py
active = []
for p, q in self.queues.items():
    active.append(p)
    q.close()
exit(active)
