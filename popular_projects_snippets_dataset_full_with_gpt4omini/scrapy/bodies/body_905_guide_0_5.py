from twisted.internet import reactor # pragma: no cover
from twisted.internet.task import Deferred # pragma: no cover
import threading # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
self._timeout_cl = threading.Event() # pragma: no cover
self._timeout_cl.set() # pragma: no cover
self._txresponse = type('MockResponse', (object,), {'_transport': type('MockTransport', (object,), {'stopProducing': lambda self: None})()})() # pragma: no cover
result = 'some_result' # pragma: no cover
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
