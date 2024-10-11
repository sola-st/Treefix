from types import SimpleNamespace # pragma: no cover

self = SimpleNamespace() # pragma: no cover
self.request = SimpleNamespace(cb_kwargs='mocked_value') # pragma: no cover

from types import SimpleNamespace # pragma: no cover

self = SimpleNamespace() # pragma: no cover
self.request = SimpleNamespace(cb_kwargs={}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/response/__init__.py
from l3.Runtime import _l_
try:
    _l_(4687)

    aux = self.request.cb_kwargs
    _l_(4684)
    exit(aux)
except AttributeError:
    _l_(4686)

    raise AttributeError(
        "Response.cb_kwargs not available, this response "
        "is not tied to any request"
    )
    _l_(4685)
