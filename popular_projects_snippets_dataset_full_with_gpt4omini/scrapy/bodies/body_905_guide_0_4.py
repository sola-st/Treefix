from twisted.internet import reactor # pragma: no cover

class MockTimeoutCl: # pragma: no cover
    def active(self): return True # pragma: no cover
    def cancel(self): pass # pragma: no cover
 # pragma: no cover
class MockTxResponse: # pragma: no cover
    class MockTransport: # pragma: no cover
        def stopProducing(self): pass # pragma: no cover
    _transport = MockTransport() # pragma: no cover
result = 42 # pragma: no cover
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
