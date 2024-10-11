class MockProtocolFactory: pass # pragma: no cover
class MockDeferred: # pragma: no cover
    def addCallback(self, func): # pragma: no cover
        func(MockProtocolFactory()) # pragma: no cover
    def addErrback(self, func): # pragma: no cover
        pass # pragma: no cover
class MockSuper: # pragma: no cover
    def connect(self, protocolFactory): # pragma: no cover
        return MockDeferred() # pragma: no cover
class MockTunnel: # pragma: no cover
    def __init__(self): # pragma: no cover
        self._protocolFactory = None # pragma: no cover
        self._tunnelReadyDeferred = None # pragma: no cover
    def requestTunnel(self, result): # pragma: no cover
        pass # pragma: no cover
    def connectFailed(self, result): # pragma: no cover
        pass # pragma: no cover
tunnel_instance = MockTunnel() # pragma: no cover
super_instance = MockSuper() # pragma: no cover
tunnel_instance.__class__ = type('TunnelClass', (MockTunnel,), {'connect': super_instance.connect}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
self._protocolFactory = protocolFactory
_l_(21052)
connectDeferred = super().connect(protocolFactory)
_l_(21053)
connectDeferred.addCallback(self.requestTunnel)
_l_(21054)
connectDeferred.addErrback(self.connectFailed)
_l_(21055)
aux = self._tunnelReadyDeferred
_l_(21056)
exit(aux)
