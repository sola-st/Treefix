from types import SimpleNamespace # pragma: no cover
import sys # pragma: no cover

crawler = SimpleNamespace() # pragma: no cover
cls = lambda x: sys.exit if x == crawler else None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/request.py
from l3.Runtime import _l_
aux = cls(crawler)
_l_(19984)
exit(aux)
