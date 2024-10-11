from typing import Any, Dict # pragma: no cover
import time # pragma: no cover

class MockTimeoutCL: # pragma: no cover
    def __init__(self, active: bool): # pragma: no cover
        self._active = active # pragma: no cover
 # pragma: no cover
    def active(self): # pragma: no cover
        return self._active # pragma: no cover
 # pragma: no cover
    def cancel(self): # pragma: no cover
        self._active = False # pragma: no cover
 # pragma: no cover
class MockTxResponse: # pragma: no cover
    def __init__(self): # pragma: no cover
        self._transport = type('MockTransport', (object,), {'stopProducing': lambda: print('Producing stopped')})() # pragma: no cover
 # pragma: no cover
class MockClass: # pragma: no cover
    def __init__(self, timeout_cl: bool): # pragma: no cover
        self._timeout_cl = MockTimeoutCL(timeout_cl) # pragma: no cover
        self._txresponse = MockTxResponse() # pragma: no cover
 # pragma: no cover
self = MockClass(timeout_cl=True) # pragma: no cover
result = 'result_value' # pragma: no cover
url = 'http://example.com' # pragma: no cover
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
