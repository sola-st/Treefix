self = type('MockSelf', (object,), {})() # pragma: no cover
self.request = type('MockRequest', (object,), {'cb_kwargs': {}})() # pragma: no cover

self = type('MockSelf', (object,), {'request': None})() # pragma: no cover
self.request = type('MockRequest', (object,), {'cb_kwargs': {}})() # pragma: no cover
self.request.cb_kwargs = {} # pragma: no cover

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
