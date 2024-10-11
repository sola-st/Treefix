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

import sys # pragma: no cover

dnscache = {'example.com': ['1.2.3.4', '5.6.7.8']} # pragma: no cover
hostName = 'example.com' # pragma: no cover
portNumber = 80 # pragma: no cover
addressTypes = ['IPv4', 'IPv6'] # pragma: no cover
transportSemantics = 'TCP' # pragma: no cover
class HostResolution: # pragma: no cover
    def __init__(self, hostName): # pragma: no cover
        self.hostName = hostName # pragma: no cover
class MockResolutionReceiver: # pragma: no cover
    def resolutionBegan(self, hostResolution): # pragma: no cover
        print(f'resolutionBegan called with {hostResolution.hostName}') # pragma: no cover
    def addressResolved(self, addr): # pragma: no cover
        print(f'addressResolved called with {addr}') # pragma: no cover
    def resolutionComplete(self): # pragma: no cover
        print('resolutionComplete called') # pragma: no cover
self = type('MockResolverWrapper', (object,), {'original_resolver': type('MockResolver', (object,), {'resolveHostName': lambda *args: print('resolveHostName called')})()})() # pragma: no cover
resolutionReceiver = MockResolutionReceiver() # pragma: no cover
_CachingResolutionReceiver = type('_CachingResolutionReceiver', (object,), {'__init__': lambda self, receiver, host: None}) # pragma: no cover

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
