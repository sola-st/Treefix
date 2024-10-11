from unittest.mock import Mock # pragma: no cover

self = type('MockSelf', (object,), {'resolutionReceiver': Mock(resolutionReceiver=Mock(addressResolved=Mock())), 'addresses': []})() # pragma: no cover
address = '123 Main St' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/resolver.py
from l3.Runtime import _l_
self.resolutionReceiver.addressResolved(address)
_l_(9335)
self.addresses.append(address)
_l_(9336)
