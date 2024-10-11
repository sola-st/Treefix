import time # pragma: no cover
import pickle # pragma: no cover

import time # pragma: no cover
import pickle # pragma: no cover

class MockFingerprinter:# pragma: no cover
    def fingerprint(self, request):# pragma: no cover
        return b'some_fingerprint' # pragma: no cover
class MockDB:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.storage = {}# pragma: no cover
    def __contains__(self, item):# pragma: no cover
        return item in self.storage# pragma: no cover
    def __getitem__(self, item):# pragma: no cover
        return self.storage[item]# pragma: no cover
    def __setitem__(self, key, value):# pragma: no cover
        self.storage[key] = value # pragma: no cover
self = type('Mock', (object,), {'_fingerprinter': MockFingerprinter(), 'db': MockDB(), 'expiration_secs': 3600})() # pragma: no cover
request = 'example_request' # pragma: no cover
db = self.db# pragma: no cover
self.db['some_fingerprint_time'] = time.time() - 1000  # some time ago# pragma: no cover
self.db['some_fingerprint_data'] = pickle.dumps('example_data') # pragma: no cover
time = time.time# pragma: no cover
pickle = pickle # pragma: no cover

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
