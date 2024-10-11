self = type('Mock', (object,), {})() # pragma: no cover
self.jar = type('Mock', (object,), {'_cookies': []})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/cookies.py
from l3.Runtime import _l_
aux = self.jar._cookies
_l_(16776)
exit(aux)
