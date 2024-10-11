import sys # pragma: no cover
from types import SimpleNamespace # pragma: no cover

cls = SimpleNamespace # pragma: no cover
crawler = SimpleNamespace(settings=SimpleNamespace()) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/redirect.py
from l3.Runtime import _l_
aux = cls(crawler.settings)
_l_(20930)
exit(aux)
