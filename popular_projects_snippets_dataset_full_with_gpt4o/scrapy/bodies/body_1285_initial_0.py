import sys # pragma: no cover

cls = sys # pragma: no cover
crawler = type('Mock', (object,), {'settings': {}})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/redirect.py
from l3.Runtime import _l_
aux = cls(crawler.settings)
_l_(20930)
exit(aux)
