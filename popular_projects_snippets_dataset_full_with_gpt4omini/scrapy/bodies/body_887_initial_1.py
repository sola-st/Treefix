from unittest.mock import MagicMock # pragma: no cover

class DummyClass: pass# pragma: no cover
cls = DummyClass # pragma: no cover
crawler = MagicMock()# pragma: no cover
crawler.settings = {'setting1': 'value1', 'setting2': 'value2'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
aux = cls(crawler.settings, crawler)
_l_(7716)
exit(aux)
