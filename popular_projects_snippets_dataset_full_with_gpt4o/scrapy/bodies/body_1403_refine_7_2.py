from types import SimpleNamespace # pragma: no cover

startprios = [1, 2, 3] # pragma: no cover
self = type('Mock', (object,), {'queues': {}, 'qfactory': lambda priority: f'queue_{priority}', 'curprio': None})() # pragma: no cover

startprios = [1, 2, 3] # pragma: no cover
self = type('Mock', (object,), {# pragma: no cover
'queues': {},# pragma: no cover
'qfactory': lambda self, priority: f'queue_{priority}',# pragma: no cover
'curprio': None# pragma: no cover
})() # pragma: no cover

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
