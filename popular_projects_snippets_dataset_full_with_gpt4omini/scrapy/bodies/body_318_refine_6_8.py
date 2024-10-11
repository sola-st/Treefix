import time # pragma: no cover
import pickle # pragma: no cover

import time # pragma: no cover
import pickle # pragma: no cover

class MockFingerprinter:# pragma: no cover
    def fingerprint(self, request):# pragma: no cover
        return b'some_fingerprint' # pragma: no cover
class MockDatabase:  # Mock database to hold the fingerprints and data# pragma: no cover
    def __init__(self):# pragma: no cover
        self.store = {}# pragma: no cover
    def __setitem__(self, key, value):# pragma: no cover
        self.store[key] = value# pragma: no cover
    def __getitem__(self, key):# pragma: no cover
        return self.store[key]# pragma: no cover
    def __contains__(self, key):# pragma: no cover
        return key in self.store# pragma: no cover
# pragma: no cover
self = type('Mock', (object,), {'_fingerprinter': MockFingerprinter(), 'db': MockDatabase(), 'expiration_secs': 3600})() # pragma: no cover
request = 'example_request' # pragma: no cover
time = lambda: 1000000000.0 # pragma: no cover
pickle = type('MockPickle', (object,), {'loads': lambda x: x})() # pragma: no cover
self.db['some_fingerprint_time'] = 999999998.0 # pragma: no cover
self.db['some_fingerprint_data'] = b'some_data' # pragma: no cover

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
