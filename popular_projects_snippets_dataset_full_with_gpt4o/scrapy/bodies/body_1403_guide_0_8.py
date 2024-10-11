import sys # pragma: no cover

startprios = [] # pragma: no cover
type('MockQueueFactory', (object,), {'__call__': lambda self, priority: None}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/pqueues.py
from l3.Runtime import _l_
if not startprios:
    _l_(20790)

    exit()
    _l_(20789)

for priority in startprios:
    _l_(20792)

    self.queues[priority] = self.qfactory(priority)
    _l_(20791)

self.curprio = min(startprios)
_l_(20793)
