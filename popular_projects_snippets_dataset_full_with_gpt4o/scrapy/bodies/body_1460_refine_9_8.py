from typing import List # pragma: no cover

dnscache = {'example.com': ['93.184.216.34']} # pragma: no cover
hostName = 'example.com' # pragma: no cover
self = type('MockResolver', (object,), {'original_resolver': type('MockOriginalResolver', (object,), {'resolveHostName': lambda *args: 'Resolution initiated'})()})() # pragma: no cover
_CachingResolutionReceiver = lambda resolutionReceiver, hostName: 'ResolutionReceiver for ' + hostName # pragma: no cover
resolutionReceiver = type('MockResolutionReceiver', (object,), {'resolutionBegan': lambda self, resolution: print(f'Resolution began for {resolution.hostName}'), 'addressResolved': lambda self, addr: print(f'Address resolved: {addr}'), 'resolutionComplete': lambda self: print('Resolution complete')})() # pragma: no cover
portNumber = 80 # pragma: no cover
addressTypes = ['IPv4', 'IPv6'] # pragma: no cover
transportSemantics = 'TCP' # pragma: no cover
HostResolution = lambda hostName: type('HostResolutionClass', (object,), {'hostName': hostName})(hostName) # pragma: no cover

from typing import List # pragma: no cover

dnscache = {'example.com': ['93.184.216.34']} # pragma: no cover
hostName = 'example.com' # pragma: no cover
self = type('MockResolver', (object,), {'original_resolver': type('MockOriginalResolver', (object,), {'resolveHostName': lambda *args: 'Resolution initiated'})()})() # pragma: no cover
_CachingResolutionReceiver = lambda resolutionReceiver, hostName: 'ResolutionReceiver for ' + hostName # pragma: no cover
resolutionReceiver = type('MockResolutionReceiver', (object,), {'resolutionBegan': lambda self, resolution: print(f'Resolution began for {resolution.hostName}'), 'addressResolved': lambda self, addr: print(f'Address resolved: {addr}'), 'resolutionComplete': lambda self: print('Resolution complete')})() # pragma: no cover
portNumber = 80 # pragma: no cover
addressTypes = ['IPv4', 'IPv6'] # pragma: no cover
transportSemantics = 'TCP' # pragma: no cover
HostResolution = type('HostResolutionClass', (object,), { '__init__': lambda self, hostName: setattr(self, 'hostName', hostName) }) # pragma: no cover

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
