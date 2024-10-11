from types import SimpleNamespace # pragma: no cover

self = SimpleNamespace(status='success', url='https://example.com') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/response/__init__.py
from l3.Runtime import _l_
aux = f"<{self.status} {self.url}>"
_l_(10056)
exit(aux)
