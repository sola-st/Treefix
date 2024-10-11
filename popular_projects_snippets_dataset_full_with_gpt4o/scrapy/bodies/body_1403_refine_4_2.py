startprios = [1, 2, 3] # pragma: no cover
self = type('Mock', (object,), {# pragma: no cover
'queues': {},# pragma: no cover
'qfactory': lambda priority: f'Queue_{priority}',# pragma: no cover
'curprio': None# pragma: no cover
})() # pragma: no cover

startprios = [1, 2, 3] # pragma: no cover
class MockBase:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.queues = {}# pragma: no cover
        self.curprio = None# pragma: no cover
    def qfactory(self, priority):# pragma: no cover
        return f'Queue_{priority}'# pragma: no cover
self = MockBase() # pragma: no cover

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
