self = type('Mock', (object,), {'resolutionReceiver': type('MockReceiver', (object,), {'addressResolved': lambda self, address: None})(), 'addresses': []})() # pragma: no cover
address = '123 Main St.' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/resolver.py
from l3.Runtime import _l_
self.resolutionReceiver.addressResolved(address)
_l_(20419)
self.addresses.append(address)
_l_(20420)
