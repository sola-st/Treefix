from queue import PriorityQueue # pragma: no cover

create_instance = lambda pqclass, settings, crawler, downstream_queue_cls, key: pqclass(settings, crawler, downstream_queue_cls, key) # pragma: no cover
self = type('Mock', (object,), {'pqclass': PriorityQueue, 'crawler': 'default_crawler', 'mqclass': PriorityQueue})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/scheduler.py
from l3.Runtime import _l_
""" Create a new priority queue instance, with in-memory storage """
aux = create_instance(self.pqclass,
                       settings=None,
                       crawler=self.crawler,
                       downstream_queue_cls=self.mqclass,
                       key='')
_l_(8890)
exit(aux)
