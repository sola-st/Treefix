self = type('Mock', (object,), {'method': 'GET', 'url': 'http://example.com'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/request/__init__.py
from l3.Runtime import _l_
aux = f"<{self.method} {self.url}>"
_l_(21034)
exit(aux)
