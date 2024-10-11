from twisted.internet.defer import Deferred # pragma: no cover
import sys # pragma: no cover

# Mock class to simulate the base class of the object containing the code snippet # pragma: no cover
class MockParent: # pragma: no cover
    def connect(self, protocolFactory): # pragma: no cover
        d = Deferred() # pragma: no cover
        d.callback('connected') # pragma: no cover
        return d # pragma: no cover
 # pragma: no cover
class MockProtocolFactory: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
# Simulated `self` object in the snippet # pragma: no cover
self = type('Mock', (MockParent,), {'_tunnelReadyDeferred': Deferred(), 'requestTunnel': lambda res: res, 'connectFailed': lambda err: err})() # pragma: no cover
 # pragma: no cover
# Initialization of variable used in the snippet # pragma: no cover
protocolFactory = MockProtocolFactory() # pragma: no cover
self._protocolFactory = protocolFactory # pragma: no cover

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
