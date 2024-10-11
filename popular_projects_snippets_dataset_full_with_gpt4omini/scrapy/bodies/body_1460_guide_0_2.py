from collections import defaultdict # pragma: no cover
from unittest.mock import MagicMock # pragma: no cover

dnscache = defaultdict(list) # pragma: no cover
hostName = 'example.com' # pragma: no cover
portNumber = 80 # pragma: no cover
addressTypes = [] # pragma: no cover
transportSemantics = 'TCP' # pragma: no cover
resolutionReceiver = MagicMock() # pragma: no cover
self = type('Mock', (object,), {'original_resolver': MagicMock()})() # pragma: no cover
self.original_resolver.resolveHostName = MagicMock(return_value='mock_address') # pragma: no cover

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
