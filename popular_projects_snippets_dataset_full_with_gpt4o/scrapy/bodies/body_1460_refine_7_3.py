from typing import List # pragma: no cover
import sys # pragma: no cover

dnscache = {'example.com': ['1.2.3.4', '5.6.7.8']} # pragma: no cover
hostName = 'example.com' # pragma: no cover
self = type('MockSelf', (), {'original_resolver': type('MockResolver', (), {'resolveHostName': lambda *args: None})()})() # pragma: no cover
_CachingResolutionReceiver = lambda rr, hn: None # pragma: no cover
resolutionReceiver = type('MockReceiver', (), { # pragma: no cover
    'resolutionBegan': lambda self, hr: None, # pragma: no cover
    'addressResolved': lambda self, addr: None, # pragma: no cover
})() # pragma: no cover
portNumber = 80 # pragma: no cover
addressTypes = ['A', 'AAAA'] # pragma: no cover
transportSemantics = 'TCP' # pragma: no cover
HostResolution = lambda hn: None # pragma: no cover

from typing import List # pragma: no cover
from sys import exit # pragma: no cover

dnscache = {'example.com': ['93.184.216.34']} # pragma: no cover
hostName = 'example.com' # pragma: no cover
self = type('MockSelf', (object,), {'original_resolver': type('MockResolver', (object,), {'resolveHostName': lambda *args: None})()})() # pragma: no cover
_CachingResolutionReceiver = type('MockCachingResolutionReceiver', (object,), {'__init__': lambda self, receiver, hostName: None}) # pragma: no cover
resolutionReceiver = type('MockResolutionReceiver', (object,), { # pragma: no cover
    'resolutionBegan': lambda self, hr: None, # pragma: no cover
    'addressResolved': lambda self, addr: None, # pragma: no cover
    'resolutionComplete': lambda self: None # pragma: no cover
})() # pragma: no cover
portNumber = 80 # pragma: no cover
addressTypes = ['A', 'AAAA'] # pragma: no cover
transportSemantics = 'TCP' # pragma: no cover
HostResolution = type('MockHostResolution', (object,), {'__init__': lambda self, hostName: None}) # pragma: no cover

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
