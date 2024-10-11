from twisted.internet.defer import Deferred # pragma: no cover
from twisted.protocols.basic import LineReceiver # pragma: no cover

protocolFactory = LineReceiver() # pragma: no cover
self = type('Mock', (object,), {# pragma: no cover
    '_protocolFactory': protocolFactory,# pragma: no cover
    'requestTunnel': lambda *args, **kwargs: None,# pragma: no cover
    'connectFailed': lambda *args, **kwargs: None,# pragma: no cover
    '_tunnelReadyDeferred': Deferred()# pragma: no cover
})() # pragma: no cover

from twisted.internet.defer import Deferred # pragma: no cover
from twisted.protocols.basic import LineReceiver # pragma: no cover
from twisted.internet.protocol import ClientFactory # pragma: no cover

class DummyTransport:# pragma: no cover
    def write(self, data):# pragma: no cover
        pass# pragma: no cover
    def loseConnection(self):# pragma: no cover
        pass # pragma: no cover
class SimpleProtocol(LineReceiver):# pragma: no cover
    def connectionMade(self):# pragma: no cover
        print('Connection made!')# pragma: no cover
    def connectionLost(self, reason):# pragma: no cover
        print('Connection lost!') # pragma: no cover
class SimpleClientFactory(ClientFactory):# pragma: no cover
    def buildProtocol(self, addr):# pragma: no cover
        return SimpleProtocol() # pragma: no cover
class MockBase:# pragma: no cover
    def connect(self, protocolFactory):# pragma: no cover
        proto = protocolFactory.buildProtocol(None)# pragma: no cover
        proto.makeConnection(DummyTransport())# pragma: no cover
        d = Deferred()# pragma: no cover
        d.callback(proto)# pragma: no cover
        return d # pragma: no cover
protocolFactory = SimpleClientFactory() # pragma: no cover
self = type('Mock', (MockBase,), {# pragma: no cover
    '_protocolFactory': protocolFactory,# pragma: no cover
    'requestTunnel': lambda *args, **kwargs: None,# pragma: no cover
    'connectFailed': lambda *args, **kwargs: None,# pragma: no cover
    '_tunnelReadyDeferred': Deferred()# pragma: no cover
})() # pragma: no cover

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
