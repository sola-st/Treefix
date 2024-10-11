import types # pragma: no cover

cls = type('MockCls', (object,), {}) # pragma: no cover
crawler = type('MockCrawler', (object,), {'settings': {}})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
aux = cls(crawler.settings, crawler)
_l_(18576)
exit(aux)
