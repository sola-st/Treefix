from twisted.internet.defer import Deferred # pragma: no cover
from twisted.internet.protocol import Protocol # pragma: no cover
from twisted.internet.protocol import ClientFactory # pragma: no cover

protocolFactory = ClientFactory() # pragma: no cover
self = type('Mock', (object,), {'_protocolFactory': None, 'requestTunnel': lambda self, x: print('Tunnel requested'), 'connectFailed': lambda self, x: print('Connection failed'), '_tunnelReadyDeferred': Deferred()})() # pragma: no cover
self._protocolFactory = protocolFactory # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
self._protocolFactory = protocolFactory
_l_(9836)
connectDeferred = super().connect(protocolFactory)
_l_(9837)
connectDeferred.addCallback(self.requestTunnel)
_l_(9838)
connectDeferred.addErrback(self.connectFailed)
_l_(9839)
aux = self._tunnelReadyDeferred
_l_(9840)
exit(aux)
