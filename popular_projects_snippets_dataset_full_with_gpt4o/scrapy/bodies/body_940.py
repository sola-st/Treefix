# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/webclient.py
from l3.Runtime import _l_
p = ClientFactory.buildProtocol(self, addr)
_l_(21116)
p.followRedirect = self.followRedirect
_l_(21117)
p.afterFoundGet = self.afterFoundGet
_l_(21118)
if self.timeout:
    _l_(21123)

    try:
        from twisted.internet import reactor
        _l_(21120)

    except ImportError:
        pass
    timeoutCall = reactor.callLater(self.timeout, p.timeout)
    _l_(21121)
    self.deferred.addBoth(self._cancelTimeout, timeoutCall)
    _l_(21122)
aux = p
_l_(21124)
exit(aux)
