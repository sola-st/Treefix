from typing import List # pragma: no cover
class HostResolution: # pragma: no cover
    def __init__(self, hostName): # pragma: no cover
        self.hostName = hostName # pragma: no cover

dnscache = {'example.com': ['192.168.1.1', '192.168.1.2']} # pragma: no cover
hostName = 'example.com' # pragma: no cover
self = type('Mock', (object,), {'original_resolver': type('Mock', (object,), {'resolveHostName': lambda *args: None})()})() # pragma: no cover
_CachingResolutionReceiver = lambda *args: None # pragma: no cover
resolutionReceiver = type('Mock', (object,), { # pragma: no cover
    'resolutionBegan': lambda self, *args: None, # pragma: no cover
    'addressResolved': lambda self, *args: None, # pragma: no cover
    'resolutionComplete': lambda self, *args: None # pragma: no cover
})() # pragma: no cover
portNumber = 80 # pragma: no cover
addressTypes = ['IPv4', 'IPv6'] # pragma: no cover
transportSemantics = 'TCP' # pragma: no cover

import sys # pragma: no cover

dnscache = {'example.com': ['192.0.2.1', '192.0.2.2']} # pragma: no cover
hostName = 'example.com' # pragma: no cover
portNumber = 80 # pragma: no cover
addressTypes = ['IPv4'] # pragma: no cover
transportSemantics = 'tcp' # pragma: no cover
class HostResolution: # pragma: no cover
    def __init__(self, hostName): # pragma: no cover
        self.hostName = hostName # pragma: no cover
class _CachingResolutionReceiver: # pragma: no cover
    def __init__(self, receiver, host): # pragma: no cover
        pass # pragma: no cover
class MockResolver: # pragma: no cover
    def resolveHostName(self, receiver, host, port, types, semantics): # pragma: no cover
        print(f'Mocked resolveHostName called for {host}:{port}') # pragma: no cover
self = type('MockSelf', (object,), { # pragma: no cover
    'original_resolver': MockResolver() # pragma: no cover
})() # pragma: no cover
resolutionReceiver = type('MockReceiver', (object,), { # pragma: no cover
    'resolutionBegan': lambda self, hr: print(f'resolutionBegan called with {hr.hostName}'), # pragma: no cover
    'addressResolved': lambda self, addr: print(f'Address resolved: {addr}'), # pragma: no cover
    'resolutionComplete': lambda self: print('Resolution complete') # pragma: no cover
})() # pragma: no cover
exit = sys.exit # pragma: no cover

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
