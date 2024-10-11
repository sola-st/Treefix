import time # pragma: no cover
import pickle # pragma: no cover

class MockFingerprinter: # pragma: no cover
    def fingerprint(self, request): # pragma: no cover
        return b'unique_fingerprint' # pragma: no cover
 # pragma: no cover
class MockDB: # pragma: no cover
    def __init__(self, data): # pragma: no cover
        self.data = data # pragma: no cover
    def __contains__(self, key): # pragma: no cover
        return key in self.data # pragma: no cover
    def __getitem__(self, key): # pragma: no cover
        return self.data[key] # pragma: no cover
    def __setitem__(self, key, value): # pragma: no cover
        self.data[key] = value # pragma: no cover
 # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    '_fingerprinter': MockFingerprinter(), # pragma: no cover
    'db': MockDB({ # pragma: no cover
        'unique_fingerprint_time': str(time.time() - 20), # pragma: no cover
        'unique_fingerprint_data': pickle.dumps('mock_data') # pragma: no cover
    }), # pragma: no cover
    'expiration_secs': 10 # pragma: no cover
})() # pragma: no cover
request = 'dummy_request' # pragma: no cover

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
