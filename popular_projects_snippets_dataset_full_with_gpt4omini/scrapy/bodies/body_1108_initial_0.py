import http.cookies # pragma: no cover

class MockJar:  # A mock class to simulate jar behavior # pragma: no cover
    def __init__(self): # pragma: no cover
        self._cookies = http.cookies.SimpleCookie() # pragma: no cover
        self._cookies['session_id'] = 'abc123' # pragma: no cover
self = type('Mock', (object,), {'jar': MockJar()})()  # Initializing 'self' with a mock class instance # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/cookies.py
from l3.Runtime import _l_
aux = self.jar._cookies
_l_(5107)
exit(aux)
