import asyncio # pragma: no cover
from unittest.mock import Mock # pragma: no cover
import sys # pragma: no cover

self = Mock() # pragma: no cover
self._timeout_cl = Mock(active=lambda: True, cancel=lambda: None) # pragma: no cover
self._txresponse = Mock(_transport=Mock(stopProducing=lambda: None)) # pragma: no cover
url = 'http://example.com' # pragma: no cover
timeout = 10 # pragma: no cover
result = 'Timeout reached' # pragma: no cover
sys.exit = lambda x: x # pragma: no cover

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
