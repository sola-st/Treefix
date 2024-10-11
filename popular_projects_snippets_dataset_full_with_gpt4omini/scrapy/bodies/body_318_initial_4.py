import time # pragma: no cover
import pickle # pragma: no cover

class MockFingerprinter:# pragma: no cover
    def fingerprint(self, request): return b'sample_fingerprint' # pragma: no cover
key = 'sample_fingerprint_hex'# pragma: no cover
self = type('Mock', (object,), {'_fingerprinter': MockFingerprinter(), 'db': {}, 'expiration_secs': 100})() # pragma: no cover
request = 'sample_request' # pragma: no cover
db = {f'{key}_time': time.time(), f'{key}_data': pickle.dumps({'data': 'sample_data'})} # pragma: no cover
db[f'{key}_time'] = time.time() - 50 # pragma: no cover

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
