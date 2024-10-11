from typing import Dict, List, Any # pragma: no cover
class HostResolution: pass # pragma: no cover

dnscache: Dict[str, List[str]] = {'example.com': ['192.0.2.1', '192.0.2.2']} # pragma: no cover
hostName: str = 'example.com' # pragma: no cover
portNumber: int = 80 # pragma: no cover
addressTypes: List[str] = ['A', 'AAAA'] # pragma: no cover
transportSemantics: str = 'TCP' # pragma: no cover

from typing import Dict, List, Any # pragma: no cover

dnscache: Dict[str, List[str]] = {'example.com': ['93.184.216.34', '2606:4700:4802:40::6818:1cf']} # pragma: no cover
hostName: str = 'example.com' # pragma: no cover
class MockOriginalResolver:  # Mock class for the original resolver# pragma: no cover
    def resolveHostName(self, receiver, hostName, portNumber, addressTypes, transportSemantics):# pragma: no cover
        return None # pragma: no cover
self: Any = type('MockSelf', (object,), {'original_resolver': MockOriginalResolver()})() # pragma: no cover
_CachingResolutionReceiver = type('MockCachingResolutionReceiver', (object,), {'__init__': lambda self, receiver, hostName: None}) # pragma: no cover
resolutionReceiver: Any = type('MockResolutionReceiver', (object,), {  # Mock receiver# pragma: no cover
        'resolutionBegan': lambda self, resolution: None,# pragma: no cover
        'addressResolved': lambda self, addr: None,# pragma: no cover
        'resolutionComplete': lambda self: None# pragma: no cover
    })() # pragma: no cover
portNumber: int = 80 # pragma: no cover
addressTypes: List[str] = ['A', 'AAAA'] # pragma: no cover
transportSemantics: str = 'UDP' # pragma: no cover
class HostResolution:  # Define a simple class for HostResolution# pragma: no cover
    def __init__(self, hostName: str):# pragma: no cover
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
