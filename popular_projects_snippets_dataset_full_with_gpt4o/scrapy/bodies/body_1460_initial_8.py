import sys # pragma: no cover
from collections import defaultdict # pragma: no cover

dnscache = defaultdict(list, {'example.com': ['192.168.1.1']}) # pragma: no cover
hostName = 'example.com' # pragma: no cover
portNumber = 80 # pragma: no cover
addressTypes = ['IPv4', 'IPv6'] # pragma: no cover
transportSemantics = 'TCP' # pragma: no cover
HostResolution = lambda x: x # pragma: no cover
resolutionReceiver = type('Mock', (object,), { # pragma: no cover
    'resolutionBegan': lambda self, x: None, # pragma: no cover
    'addressResolved': lambda self, x: None, # pragma: no cover
    'resolutionComplete': lambda self: None # pragma: no cover
})() # pragma: no cover
self = type('SelfMock', (object,), { # pragma: no cover
    'original_resolver': type('OriginalResolverMock', (object,), { # pragma: no cover
        'resolveHostName': lambda self, *args: None # pragma: no cover
    })() # pragma: no cover
})() # pragma: no cover
_CachingResolutionReceiver = lambda *args: None # pragma: no cover

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
