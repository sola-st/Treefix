cls = type('MockClass', (object,), {}) # pragma: no cover
crawler = 'CrawlerInstance' # pragma: no cover
downstream_queue_cls = type('MockQueueClass', (object,), {}) # pragma: no cover
key = 'unique-key' # pragma: no cover
startprios = [1, 2, 3] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/pqueues.py
from l3.Runtime import _l_
aux = cls(crawler, downstream_queue_cls, key, startprios)
_l_(18416)
exit(aux)
