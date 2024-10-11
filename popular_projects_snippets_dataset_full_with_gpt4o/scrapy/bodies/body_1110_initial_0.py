self = type('Mock', (object,), {'jar': type('Mock', (object,), {'clear': lambda self, domain, path, name: 0})()})() # pragma: no cover
domain = 'example.com' # pragma: no cover
path = '/' # pragma: no cover
name = 'session_id' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/cookies.py
from l3.Runtime import _l_
aux = self.jar.clear(domain, path, name)
_l_(15556)
exit(aux)
