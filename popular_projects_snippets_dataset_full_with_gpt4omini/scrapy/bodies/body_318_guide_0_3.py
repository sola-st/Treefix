import pickle # pragma: no cover
import time # pragma: no cover
from typing import Dict, Any # pragma: no cover

class MockDB(Dict[str, Any]): pass # pragma: no cover
self = type('Mock', (object,), {'_fingerprinter': type('MockFingerprinter', (object,), {'fingerprint': lambda self, request: b'some_fingerprint'})(), 'db': MockDB({'some_fingerprint_time': '0', 'some_fingerprint_data': pickle.dumps('some_data')}), 'expiration_secs': 5})() # pragma: no cover
request = 'some_request' # pragma: no cover

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
