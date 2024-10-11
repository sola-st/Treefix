from unittest.mock import Mock # pragma: no cover

self = type('MockSelf', (object,), {'jar': Mock()})() # pragma: no cover
domain = 'example.com' # pragma: no cover
path = '/path/to/resource' # pragma: no cover
name = 'cookie_name' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/cookies.py
from l3.Runtime import _l_
aux = self.jar.clear(domain, path, name)
_l_(4032)
exit(aux)
