from collections import deque # pragma: no cover

class MockCrawler: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.data = 'some data' # pragma: no cover
 # pragma: no cover
class MockDownstreamQueue: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.queue = deque() # pragma: no cover
 # pragma: no cover
class MockClass: # pragma: no cover
    def __init__(self, crawler, queue_cls, key, prios): # pragma: no cover
        self.crawler = crawler # pragma: no cover
        self.queue = queue_cls() # pragma: no cover
        self.key = key # pragma: no cover
        self.startprios = prios # pragma: no cover
 # pragma: no cover
cls = MockClass # pragma: no cover
crawler = MockCrawler() # pragma: no cover
downstream_queue_cls = MockDownstreamQueue # pragma: no cover
key = 'example_key' # pragma: no cover
startprios = [1, 2, 3, 4, 5] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/pqueues.py
from l3.Runtime import _l_
aux = cls(crawler, downstream_queue_cls, key, startprios)
_l_(18416)
exit(aux)
