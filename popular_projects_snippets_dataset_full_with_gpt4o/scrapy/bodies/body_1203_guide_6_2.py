import sys # pragma: no cover

class MockRequest: # pragma: no cover
    def __init__(self): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
self = type('Mock', (object,), {'request': MockRequest()})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/response/__init__.py
from l3.Runtime import _l_
try:
    _l_(15958)

    aux = self.request.cb_kwargs
    _l_(15955)
    exit(aux)
except AttributeError:
    _l_(15957)

    raise AttributeError(
        "Response.cb_kwargs not available, this response "
        "is not tied to any request"
    )
    _l_(15956)
