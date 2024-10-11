import sys # pragma: no cover
from unittest.mock import Mock # pragma: no cover

timeout_cl = Mock() # pragma: no cover
timeout_cl.active.return_value = True # pragma: no cover
timeout_cl.cancel.return_value = None # pragma: no cover
transport = Mock() # pragma: no cover
transport.stopProducing.return_value = None # pragma: no cover
txresponse = Mock() # pragma: no cover
txresponse._transport = transport # pragma: no cover
self = type('Mock', (object,), {'_timeout_cl': timeout_cl, '_txresponse': txresponse})() # pragma: no cover
result = 'result_value' # pragma: no cover
url = 'http://example.com' # pragma: no cover
timeout = 5 # pragma: no cover
sys.exit = lambda x: print(f'exit called with {x}') # pragma: no cover

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
