from types import SimpleNamespace # pragma: no cover

create_instance = lambda *args, **kwargs: None # pragma: no cover
self = SimpleNamespace(pqclass=type('PriorityQueue', (object,), {}), crawler=type('Crawler', (object,), {}), mqclass=type('DownstreamQueue', (object,), {})) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/scheduler.py
from l3.Runtime import _l_
""" Create a new priority queue instance, with in-memory storage """
aux = create_instance(self.pqclass,
                       settings=None,
                       crawler=self.crawler,
                       downstream_queue_cls=self.mqclass,
                       key='')
_l_(19983)
exit(aux)
