from unittest.mock import Mock # pragma: no cover

cls = type('MockClass', (object,), {}) # pragma: no cover
crawler = Mock() # pragma: no cover
crawler.settings = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/redirect.py
from l3.Runtime import _l_
aux = cls(crawler.settings)
_l_(9555)
exit(aux)
