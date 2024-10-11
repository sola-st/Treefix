from collections import defaultdict # pragma: no cover

startprios = [1, 2, 3] # pragma: no cover
self = type('Mock', (object,), {'queues': {}, 'qfactory': lambda priority: f'Queue-{priority}'})() # pragma: no cover

from collections import defaultdict # pragma: no cover

startprios = [1, 2, 3] # pragma: no cover
self = type('Mock', (object,), {'queues': {}, 'qfactory': lambda self, priority: f'Queue for {priority}', 'curprio': None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/pqueues.py
from l3.Runtime import _l_
if not startprios:
    _l_(9663)

    exit()
    _l_(9662)

for priority in startprios:
    _l_(9665)

    self.queues[priority] = self.qfactory(priority)
    _l_(9664)

self.curprio = min(startprios)
_l_(9666)
