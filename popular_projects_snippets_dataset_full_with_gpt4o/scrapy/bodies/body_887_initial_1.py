from types import SimpleNamespace # pragma: no cover

cls = type('MockClass', (object,), {'__init__': lambda self, settings, crawler: None}) # pragma: no cover
crawler = SimpleNamespace(settings={}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
aux = cls(crawler.settings, crawler)
_l_(18576)
exit(aux)
