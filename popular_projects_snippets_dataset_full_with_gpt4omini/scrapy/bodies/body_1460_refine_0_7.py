from typing import Dict, List, Any, Optional # pragma: no cover

dnscache = {'example.com': ['192.0.2.1', '192.0.2.2']} # pragma: no cover
hostName = 'example.com' # pragma: no cover
class MockResolver:  # Mock class for original_resolver# pragma: no cover
    def resolveHostName(self, receiver, hostName, portNumber, addressTypes, transportSemantics):# pragma: no cover
        return 'Resolved' # pragma: no cover
self = type('Mock', (), {'original_resolver': MockResolver()})() # pragma: no cover
class _CachingResolutionReceiver:# pragma: no cover
    def __init__(self, receiver, hostName):# pragma: no cover
        self.receiver = receiver# pragma: no cover
        self.hostName = hostName # pragma: no cover
resolutionReceiver = type('Mock', (object,), {# pragma: no cover
        'resolutionBegan': lambda self, resolution: None,# pragma: no cover
        'addressResolved': lambda self, addr: None,# pragma: no cover
        'resolutionComplete': lambda self: None# pragma: no cover
    })() # pragma: no cover
portNumber = 53 # pragma: no cover
addressTypes = ['A', 'AAAA'] # pragma: no cover
transportSemantics = 'UDP' # pragma: no cover
class HostResolution:# pragma: no cover
    def __init__(self, hostName):# pragma: no cover
        self.hostName = hostName # pragma: no cover

from typing import Dict, List, Any # pragma: no cover

dnscache = {'example.com': ['192.0.2.1', '192.0.2.2']} # pragma: no cover
hostName = 'example.com' # pragma: no cover
class MockResolver:  # Mock class for original_resolver# pragma: no cover
    def resolveHostName(self, receiver, hostName, portNumber, addressTypes, transportSemantics):# pragma: no cover
        return 'Resolved' # pragma: no cover
self = type('Mock', (), {'original_resolver': MockResolver()})() # pragma: no cover
class _CachingResolutionReceiver:# pragma: no cover
    def __init__(self, receiver, hostName):# pragma: no cover
        self.receiver = receiver# pragma: no cover
        self.hostName = hostName # pragma: no cover
resolutionReceiver = type('Mock', (object,), {# pragma: no cover
        'resolutionBegan': lambda self, resolution: print(f'Resolution began for {resolution.hostName}'),# pragma: no cover
        'addressResolved': lambda self, addr: print(f'Address resolved: {addr}'),# pragma: no cover
        'resolutionComplete': lambda self: print('Resolution complete')# pragma: no cover
    })() # pragma: no cover
portNumber = 53 # pragma: no cover
addressTypes = ['A', 'AAAA'] # pragma: no cover
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
