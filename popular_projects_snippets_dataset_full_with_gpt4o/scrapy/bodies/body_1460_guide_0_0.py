from typing import List # pragma: no cover
from socket import gaierror # pragma: no cover

class MockOriginalResolver: # pragma: no cover
    def resolveHostName(self, receiver, hostName, portNumber, addressTypes, transportSemantics): # pragma: no cover
        receiver.resolutionBegan(HostResolution(hostName)) # pragma: no cover
        receiver.addressResolved('127.0.0.1') # pragma: no cover
        receiver.resolutionComplete() # pragma: no cover
        return 0 # pragma: no cover
 # pragma: no cover
class MockReceiver: # pragma: no cover
    def resolutionBegan(self, resolution): # pragma: no cover
        print(f'Resolution began for: {resolution.hostName}') # pragma: no cover
 # pragma: no cover
    def addressResolved(self, addr): # pragma: no cover
        print(f'Address resolved: {addr}') # pragma: no cover
 # pragma: no cover
    def resolutionComplete(self): # pragma: no cover
        print('Resolution complete') # pragma: no cover
 # pragma: no cover
class HostResolution: # pragma: no cover
    def __init__(self, hostName): # pragma: no cover
        self.hostName = hostName # pragma: no cover
 # pragma: no cover
class _CachingResolutionReceiver(MockReceiver): # pragma: no cover
    def __init__(self, receiver, hostName): # pragma: no cover
        self.receiver = receiver # pragma: no cover
        self.hostName = hostName # pragma: no cover
 # pragma: no cover
resolutionReceiver = MockReceiver() # pragma: no cover
hostName = 'example.com' # pragma: no cover
portNumber = 80 # pragma: no cover
addressTypes = [] # pragma: no cover
transportSemantics = {} # pragma: no cover
self = type('Mock', (object,), {'original_resolver': MockOriginalResolver()})() # pragma: no cover
dnscache = {} # pragma: no cover

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
