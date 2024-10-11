class MockCrawler: pass # pragma: no cover
class MockQueue: pass # pragma: no cover
cls = type('MockCrawlerManager', (object,), {}) # pragma: no cover
crawler = MockCrawler() # pragma: no cover
downstream_queue_cls = MockQueue # pragma: no cover
key = 'example-key' # pragma: no cover
startprios = [1, 2, 3] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/pqueues.py
from l3.Runtime import _l_
aux = cls(crawler, downstream_queue_cls, key, startprios)
_l_(18416)
exit(aux)
