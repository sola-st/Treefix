from types import SimpleNamespace # pragma: no cover

self = SimpleNamespace(request=SimpleNamespace(url='http://example.com')) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/cookies.py
from l3.Runtime import _l_
aux = self.request.url
_l_(16846)
exit(aux)
