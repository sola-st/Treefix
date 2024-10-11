self = type('Mock', (object,), {'status': 200, 'url': 'http://example.com'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/response/__init__.py
from l3.Runtime import _l_
aux = f"<{self.status} {self.url}>"
_l_(21467)
exit(aux)
