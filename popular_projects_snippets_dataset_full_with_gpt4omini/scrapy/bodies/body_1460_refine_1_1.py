from typing import List, Callable # pragma: no cover

dnscache = {'example.com': ['192.0.2.1', '192.0.2.2']} # pragma: no cover
hostName = 'example.com' # pragma: no cover

from typing import List, Callable # pragma: no cover

dnscache = {'example.com': ['192.0.2.1', '192.0.2.2']} # pragma: no cover
hostName = 'example.com' # pragma: no cover
class MockResolver:# pragma: no cover
    def resolveHostName(self, receiver, hostName, portNumber, addressTypes, transportSemantics):# pragma: no cover
        return 'Resolved' # pragma: no cover
self = type('MockObject', (), {'original_resolver': MockResolver()})() # pragma: no cover
_CachingResolutionReceiver = type('MockCachingResolutionReceiver', (object,), {'__init__': lambda self, receiver, hostName: None}) # pragma: no cover
class MockReceiver:# pragma: no cover
    def resolutionBegan(self, hostRes):# pragma: no cover
        print('Resolution began for:', hostRes.hostName)# pragma: no cover
    def addressResolved(self, addr):# pragma: no cover
        print('Address resolved:', addr)# pragma: no cover
    def resolutionComplete(self):# pragma: no cover
        print('Resolution complete') # pragma: no cover
resolutionReceiver = MockReceiver() # pragma: no cover
portNumber = 80 # pragma: no cover
addressTypes = ['A'] # pragma: no cover
transportSemantics = 'UDP' # pragma: no cover
class HostResolution:# pragma: no cover
    def __init__(self, hostName):# pragma: no cover
        self.hostName = hostName # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/resolver.py
from l3.Runtime import _l_
try:
    _l_(9806)

    addresses = dnscache[hostName]
    _l_(9798)
except KeyError:
    _l_(9800)

    aux = self.original_resolver.resolveHostName(
        _CachingResolutionReceiver(resolutionReceiver, hostName),
        hostName,
        portNumber,
        addressTypes,
        transportSemantics,
    )
    _l_(9799)
    exit(aux)
else:
    resolutionReceiver.resolutionBegan(HostResolution(hostName))
    _l_(9801)
    for addr in addresses:
        _l_(9803)

        resolutionReceiver.addressResolved(addr)
        _l_(9802)
    resolutionReceiver.resolutionComplete()
    _l_(9804)
    aux = resolutionReceiver
    _l_(9805)
    exit(aux)
