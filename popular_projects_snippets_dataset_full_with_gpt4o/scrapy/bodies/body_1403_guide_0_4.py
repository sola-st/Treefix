from typing import Dict, Callable, Any # pragma: no cover

class MockSelf: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.queues: Dict[int, Any] = {} # pragma: no cover
        self.qfactory: Callable[[int], Any] = lambda x: [] # pragma: no cover
        self.curprio: int = None # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover
startprios = [] # pragma: no cover

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
