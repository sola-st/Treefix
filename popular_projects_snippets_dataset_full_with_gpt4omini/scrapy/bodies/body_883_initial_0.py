from twisted.internet import defer # pragma: no cover

self = type('Mock', (), {'client': None, '_build_response': lambda self, request, protocol: None, '_failed': lambda self, request: None})() # pragma: no cover
client = type('MockClient', (), {'retrieveFile': lambda self, filepath, protocol: defer.Deferred()})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/ftp.py
from l3.Runtime import _l_
self.client = client
_l_(8225)
protocol = ReceivedDataProtocol(request.meta.get("ftp_local_filename"))
_l_(8226)
aux = client.retrieveFile(filepath, protocol).addCallbacks(
    callback=self._build_response,
    callbackArgs=(request, protocol),
    errback=self._failed,
    errbackArgs=(request,),
)
_l_(8227)
exit(aux)
