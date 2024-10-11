import sys # pragma: no cover

dnscache = {'example.com': ['192.0.2.1', '192.0.2.2']} # pragma: no cover
hostName = 'example.com' # pragma: no cover
portNumber = 80 # pragma: no cover
addressTypes = ['IPv4'] # pragma: no cover
transportSemantics = 'tcp' # pragma: no cover
HostResolution = lambda host: f'Resolving {host}' # pragma: no cover
_CachingResolutionReceiver = lambda receiver, host: f'Caching {host}' # pragma: no cover
class MockResolver: # pragma: no cover
    def resolveHostName(self, receiver, host, port, types, semantics): # pragma: no cover
        return f'Resolving {host}:{port} with types {types} over {semantics}' # pragma: no cover
self = type('MockSelf', (object,), { # pragma: no cover
    'original_resolver': MockResolver() # pragma: no cover
})() # pragma: no cover
resolutionReceiver = type('MockReceiver', (object,), { # pragma: no cover
    'resolutionBegan': lambda x: print(x), # pragma: no cover
    'addressResolved': lambda addr: print(f'Address resolved: {addr}'), # pragma: no cover
    'resolutionComplete': lambda: print('Resolution complete') # pragma: no cover
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
