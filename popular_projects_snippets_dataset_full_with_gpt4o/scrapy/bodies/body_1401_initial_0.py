from queue import Queue # pragma: no cover

cls = type('MockClass', (object,), {}) # pragma: no cover
crawler = 'dummy_crawler' # pragma: no cover
downstream_queue_cls = Queue # pragma: no cover
key = 'dummy_key' # pragma: no cover
startprios = [1, 2, 3] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/pqueues.py
from l3.Runtime import _l_
aux = cls(crawler, downstream_queue_cls, key, startprios)
_l_(18416)
exit(aux)
