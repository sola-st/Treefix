from typing import List # pragma: no cover

startprios: List[int] = [] # pragma: no cover
self = type('Mock', (object,), {'queues': {}, 'qfactory': lambda x: [], 'curprio': None})() # pragma: no cover

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
