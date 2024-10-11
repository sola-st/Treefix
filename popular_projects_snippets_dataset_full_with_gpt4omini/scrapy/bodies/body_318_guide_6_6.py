import time # pragma: no cover
import pickle # pragma: no cover
from collections import defaultdict # pragma: no cover

class MockDB(defaultdict): # pragma: no cover
    def __init__(self): # pragma: no cover
        super().__init__(bytes) # pragma: no cover
        self['abcdef_time'] = str(time.time() - 1000) # pragma: no cover
        self['abcdef_data'] = pickle.dumps('sample data') # pragma: no cover
 # pragma: no cover
class MockFingerprinter: # pragma: no cover
    def fingerprint(self, request): # pragma: no cover
        return bytes.fromhex('abcdef') # pragma: no cover
 # pragma: no cover
request = 'mock_request' # pragma: no cover
self = type('Mock', (object,), {'_fingerprinter': MockFingerprinter(), 'db': MockDB(), 'expiration_secs': 5})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/httpcache.py
from l3.Runtime import _l_
key = self._fingerprinter.fingerprint(request).hex()
_l_(10251)
db = self.db
_l_(10252)
tkey = f'{key}_time'
_l_(10253)
if tkey not in db:
    _l_(10255)

    exit()  # not found
    _l_(10254)  # not found

ts = db[tkey]
_l_(10256)
if 0 < self.expiration_secs < time() - float(ts):
    _l_(10258)

    exit()  # expired
    _l_(10257)  # expired
aux = pickle.loads(db[f'{key}_data'])
_l_(10259)

exit(aux)
