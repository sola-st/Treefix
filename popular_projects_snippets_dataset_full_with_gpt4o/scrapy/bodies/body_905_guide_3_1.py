import sys # pragma: no cover
from unittest.mock import Mock, MagicMock # pragma: no cover

class TimeoutClient: # pragma: no cover
    def active(self): # pragma: no cover
        return True # pragma: no cover
# Change this to True to trigger the first uncovered path # pragma: no cover
    def cancel(self): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
class Transport: # pragma: no cover
    def stopProducing(self): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
class TxResponse: # pragma: no cover
    def __init__(self): # pragma: no cover
        self._transport = Transport() # pragma: no cover
 # pragma: no cover
self = type('MockSelf', (object,), {'_timeout_cl': TimeoutClient(), '_txresponse': TxResponse()})() # pragma: no cover
result = 'exit_value' # pragma: no cover
url = 'http://example.com' # pragma: no cover
timeout = 10 # pragma: no cover
sys.exit = lambda x: exec(f'raise SystemExit({x})') # pragma: no cover

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
