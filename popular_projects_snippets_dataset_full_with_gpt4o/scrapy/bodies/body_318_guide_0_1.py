import pickle # pragma: no cover
import time # pragma: no cover
import hashlib # pragma: no cover

class MockFingerprinter: # pragma: no cover
    def fingerprint(self, request): # pragma: no cover
        return hashlib.sha256(request.encode()) # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def __init__(self): # pragma: no cover
        self._fingerprinter = MockFingerprinter() # pragma: no cover
        self.db = { # pragma: no cover
            'sample_key_time': str(time.time()), # pragma: no cover
            'sample_key_data': pickle.dumps('sample_data') # pragma: no cover
        } # pragma: no cover
        self.expiration_secs = 3600 # pragma: no cover
mock_self = MockSelf() # pragma: no cover
 # pragma: no cover
request = 'sample_request' # pragma: no cover
self = mock_self # pragma: no cover
time = lambda: time.time() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/httpcache.py
from l3.Runtime import _l_
key = self._fingerprinter.fingerprint(request).hex()
_l_(21569)
db = self.db
_l_(21570)
tkey = f'{key}_time'
_l_(21571)
if tkey not in db:
    _l_(21573)

    exit()  # not found
    _l_(21572)  # not found

ts = db[tkey]
_l_(21574)
if 0 < self.expiration_secs < time() - float(ts):
    _l_(21576)

    exit()  # expired
    _l_(21575)  # expired
aux = pickle.loads(db[f'{key}_data'])
_l_(21577)

exit(aux)
