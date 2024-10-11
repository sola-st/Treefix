from typing import Any, Dict, Tuple, Callable # pragma: no cover
class MockClient: # pragma: no cover
    def retrieveFile(self, filepath: str, protocol: Any) -> 'MockDeferred': # pragma: no cover
        return MockDeferred() # pragma: no cover
 # pragma: no cover
class MockDeferred: # pragma: no cover
    def addCallbacks(self, callback: Callable, callbackArgs: Tuple, errback: Callable, errbackArgs: Tuple) -> None: # pragma: no cover
        callback(*callbackArgs) # pragma: no cover
        errback(*errbackArgs) # pragma: no cover

self = type('Mock', (object,), {'client': None, '_build_response': lambda self, request, protocol: None, '_failed': lambda self, request: None})() # pragma: no cover
client = MockClient() # pragma: no cover
ReceivedDataProtocol = type('ReceivedDataProtocol', (object,), {'__init__': lambda self, filename: None}) # pragma: no cover
request = type('MockRequest', (object,), { 'meta': {'ftp_local_filename': 'example.txt'} })() # pragma: no cover
filepath = 'path/to/remote/file.txt' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/ftp.py
from l3.Runtime import _l_
self.client = client
_l_(19449)
protocol = ReceivedDataProtocol(request.meta.get("ftp_local_filename"))
_l_(19450)
aux = client.retrieveFile(filepath, protocol).addCallbacks(
    callback=self._build_response,
    callbackArgs=(request, protocol),
    errback=self._failed,
    errbackArgs=(request,),
)
_l_(19451)
exit(aux)
