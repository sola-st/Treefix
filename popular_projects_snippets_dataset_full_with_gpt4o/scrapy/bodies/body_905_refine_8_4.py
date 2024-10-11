import types # pragma: no cover

self = type('Mock', (object,), {'_timeout_cl': type('MockTimeout', (object,), {'active': lambda self: True, 'cancel': lambda self: None})(), '_txresponse': type('MockTxResponse', (object,), {'_transport': type('MockTransport', (object,), {'stopProducing': lambda self: None})()})()})() # pragma: no cover
result = 'timeout_occurred' # pragma: no cover
url = 'https://example.com' # pragma: no cover
timeout = 10 # pragma: no cover

import types # pragma: no cover
import sys # pragma: no cover

class MockSelf: # pragma: no cover
    def __init__(self): # pragma: no cover
        self._timeout_cl = types.SimpleNamespace(active=lambda: True, cancel=lambda: None) # pragma: no cover
        self._txresponse = types.SimpleNamespace( # pragma: no cover
            _transport=types.SimpleNamespace(stopProducing=lambda: None) # pragma: no cover
        ) # pragma: no cover
 # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover
result = 0 # pragma: no cover
url = 'https://example.com' # pragma: no cover
timeout = 10 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
if self._timeout_cl.active():
    _l_(17162)

    self._timeout_cl.cancel()
    _l_(17160)
    aux = result
    _l_(17161)
    exit(aux)
# needed for HTTPS requests, otherwise _ResponseReader doesn't
# receive connectionLost()
if self._txresponse:
    _l_(17164)

    self._txresponse._transport.stopProducing()
    _l_(17163)

raise TimeoutError(f"Getting {url} took longer than {timeout} seconds.")
_l_(17165)
