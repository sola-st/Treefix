from types import SimpleNamespace # pragma: no cover

class cls: pass # pragma: no cover
crawler = SimpleNamespace(settings='settings_value') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/redirect.py
from l3.Runtime import _l_
aux = cls(crawler.settings)
_l_(9555)
exit(aux)
