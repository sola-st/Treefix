import time # pragma: no cover
import pickle # pragma: no cover

import time # pragma: no cover
import pickle # pragma: no cover

class MockFingerprinter:# pragma: no cover
    def fingerprint(self, request):# pragma: no cover
        return b'abc123' # pragma: no cover
class MockDB:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.data = {}# pragma: no cover
    def __contains__(self, item):# pragma: no cover
        return item in self.data# pragma: no cover
    def __getitem__(self, item):# pragma: no cover
        return self.data[item]# pragma: no cover
    def __setitem__(self, key, value):# pragma: no cover
        self.data[key] = value# pragma: no cover
# pragma: no cover
 # pragma: no cover
db = MockDB(); db['abc123_time'] = str(time.time() - 1800)  # timestamp 30 minutes ago# pragma: no cover

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
