from queue import PriorityQueue # pragma: no cover

class MockCrawler: pass # pragma: no cover
class MockMQClass: pass # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
self.pqclass = PriorityQueue # pragma: no cover
self.crawler = MockCrawler() # pragma: no cover
self.mqclass = MockMQClass # pragma: no cover
create_instance = lambda pq_class, settings, crawler, downstream_queue_cls, key: (pq_class, settings, crawler, downstream_queue_cls, key) # pragma: no cover

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
