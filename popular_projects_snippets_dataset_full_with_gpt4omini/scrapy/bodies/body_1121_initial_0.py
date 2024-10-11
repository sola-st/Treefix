from types import SimpleNamespace # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
self.request = SimpleNamespace(url='http://example.com') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/cookies.py
from l3.Runtime import _l_
aux = self.request.url
_l_(5202)
exit(aux)
