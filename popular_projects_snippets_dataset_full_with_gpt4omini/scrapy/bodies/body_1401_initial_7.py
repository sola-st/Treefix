from queue import Queue # pragma: no cover

class MockCrawler: pass # pragma: no cover
cls = type('MockClass', (object,), {}) # pragma: no cover
crawler = MockCrawler() # pragma: no cover
downstream_queue_cls = Queue # pragma: no cover
key = 'example_key' # pragma: no cover
startprios = [1, 2, 3] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/pqueues.py
from l3.Runtime import _l_
aux = cls(crawler, downstream_queue_cls, key, startprios)
_l_(7513)
exit(aux)
