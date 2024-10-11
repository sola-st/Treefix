import pickle # pragma: no cover
import time # pragma: no cover
from unittest.mock import Mock # pragma: no cover

class MockDB: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.data = {} # pragma: no cover
        self.data['dummy_key_time'] = str(time.time() - 100) # pragma: no cover
        self.data['dummy_key_data'] = pickle.dumps('mock data') # pragma: no cover
    def __contains__(self, key): return key in self.data # pragma: no cover
    def __getitem__(self, key): return self.data[key] # pragma: no cover
 # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
self._fingerprinter = type('MockFingerprinter', (object,), {'fingerprint': lambda self, req: b'dummy_key'})() # pragma: no cover
self.db = MockDB() # pragma: no cover
request = 'mock_request' # pragma: no cover
self.expiration_secs = 10 # pragma: no cover

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
