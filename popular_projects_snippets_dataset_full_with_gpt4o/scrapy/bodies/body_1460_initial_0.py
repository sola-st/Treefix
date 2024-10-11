import socket # pragma: no cover

dnscache = {'example.com': ['93.184.216.34']} # pragma: no cover
hostName = 'example.com' # pragma: no cover
self = type('Mock', (object,), {'original_resolver': type('MockResolver', (object,), {'resolveHostName': lambda *args: None})()})() # pragma: no cover
_CachingResolutionReceiver = type('Mock', (object,), {}) # pragma: no cover
resolutionReceiver = type('Mock', (object,), {'resolutionBegan': lambda *args: None, 'addressResolved': lambda addr: None, 'resolutionComplete': lambda: None})() # pragma: no cover
portNumber = 80 # pragma: no cover
addressTypes = [socket.AF_INET] # pragma: no cover
transportSemantics = 'TCP' # pragma: no cover
HostResolution = type('Mock', (object,), {'__init__': lambda self, hostName: None}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/resolver.py
from l3.Runtime import _l_
try:
    _l_(21013)

    addresses = dnscache[hostName]
    _l_(21005)
except KeyError:
    _l_(21007)

    aux = self.original_resolver.resolveHostName(
        _CachingResolutionReceiver(resolutionReceiver, hostName),
        hostName,
        portNumber,
        addressTypes,
        transportSemantics,
    )
    _l_(21006)
    exit(aux)
else:
    resolutionReceiver.resolutionBegan(HostResolution(hostName))
    _l_(21008)
    for addr in addresses:
        _l_(21010)

        resolutionReceiver.addressResolved(addr)
        _l_(21009)
    resolutionReceiver.resolutionComplete()
    _l_(21011)
    aux = resolutionReceiver
    _l_(21012)
    exit(aux)
