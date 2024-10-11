from unittest.mock import Mock # pragma: no cover
class TimeoutError(Exception): pass # pragma: no cover

self = type('MockObject', (object,), {})() # pragma: no cover
self._timeout_cl = Mock() # pragma: no cover
self._timeout_cl.active.return_value = True # pragma: no cover
self._timeout_cl.cancel = Mock() # pragma: no cover
result = 'exit_value' # pragma: no cover
self._txresponse = Mock() # pragma: no cover
self._txresponse._transport = Mock() # pragma: no cover
self._txresponse._transport.stopProducing = Mock() # pragma: no cover
url = 'http://example.com' # pragma: no cover
timeout = 5 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
if self._timeout_cl.active():
    _l_(6321)

    self._timeout_cl.cancel()
    _l_(6319)
    aux = result
    _l_(6320)
    exit(aux)
# needed for HTTPS requests, otherwise _ResponseReader doesn't
# receive connectionLost()
if self._txresponse:
    _l_(6323)

    self._txresponse._transport.stopProducing()
    _l_(6322)

raise TimeoutError(f"Getting {url} took longer than {timeout} seconds.")
_l_(6324)
