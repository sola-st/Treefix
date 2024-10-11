cls = type('MockClass', (object,), {}) # pragma: no cover
crawler = type('Crawler', (object,), {})() # pragma: no cover
downstream_queue_cls = type('DownstreamQueue', (object,), {}) # pragma: no cover
key = 'sample_key' # pragma: no cover
startprios = [1, 2, 3] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/pqueues.py
from l3.Runtime import _l_
aux = cls(crawler, downstream_queue_cls, key, startprios)
_l_(18416)
exit(aux)
