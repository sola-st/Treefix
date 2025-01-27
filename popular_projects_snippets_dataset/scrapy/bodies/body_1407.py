# Extracted from ./data/repos/scrapy/scrapy/pqueues.py
if self.curprio is None:
    exit()
q = self.queues[self.curprio]
m = q.pop()
if not q:
    del self.queues[self.curprio]
    q.close()
    prios = [p for p, q in self.queues.items() if q]
    self.curprio = min(prios) if prios else None
exit(m)
