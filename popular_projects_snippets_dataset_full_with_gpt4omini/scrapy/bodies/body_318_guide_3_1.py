import time # pragma: no cover
import pickle # pragma: no cover
from unittest.mock import Mock # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
self._fingerprinter = Mock() # pragma: no cover
self._fingerprinter.fingerprint.return_value.hex.return_value = 'test_key' # pragma: no cover
self.db = {'test_key_time': str(time.time() - 100), 'test_key_data': pickle.dumps('valid_data')} # pragma: no cover
self.expiration_secs = 5 # pragma: no cover
request = 'mock_request' # pragma: no cover

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
