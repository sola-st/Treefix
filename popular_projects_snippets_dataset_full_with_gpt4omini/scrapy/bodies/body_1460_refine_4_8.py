from collections import defaultdict # pragma: no cover
from typing import List, Any # pragma: no cover

dnscache = defaultdict(list) # pragma: no cover
hostName = 'example.com' # pragma: no cover
class MockResolver:# pragma: no cover
    def resolveHostName(self, receiver, hostName, portNumber, addressTypes, transportSemantics):# pragma: no cover
        return None# pragma: no cover
original_resolver = MockResolver() # pragma: no cover
_CachingResolutionReceiver = type('MockCachingResolutionReceiver', (object,), {}) # pragma: no cover
resolutionReceiver = type('MockResolutionReceiver', (object,), {'resolutionBegan': lambda self, x: None, 'addressResolved': lambda self, addr: None, 'resolutionComplete': lambda self: None})() # pragma: no cover
portNumber = 80 # pragma: no cover
addressTypes = ['A', 'AAAA'] # pragma: no cover
transportSemantics = 'TCP' # pragma: no cover
HostResolution = type('MockHostResolution', (object,), {'__init__': lambda self, name: None}) # pragma: no cover

from collections import defaultdict # pragma: no cover
from typing import List # pragma: no cover

dnscache = defaultdict(list, {'example.com': ['192.0.2.1', '198.51.100.1']}) # pragma: no cover
hostName = 'example.com' # pragma: no cover
class MockOriginalResolver:# pragma: no cover
    def resolveHostName(self, receiver, hostName, portNumber, addressTypes, transportSemantics):# pragma: no cover
        return 'Resolved' # pragma: no cover
self = type('MockSelf', (object,), {'original_resolver': MockOriginalResolver()})() # pragma: no cover
_CachingResolutionReceiver = type('MockCachingResolutionReceiver', (object,), {}) # pragma: no cover
resolutionReceiver = type('MockResolutionReceiver', (object,), {# pragma: no cover
        'resolutionBegan': lambda self, hostRes: print(f'Resolution began for {hostRes.hostName}'),# pragma: no cover
        'addressResolved': lambda self, addr: print(f'Address resolved: {addr}'),# pragma: no cover
        'resolutionComplete': lambda self: print('Resolution complete')# pragma: no cover
    })() # pragma: no cover
portNumber = 80 # pragma: no cover
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
