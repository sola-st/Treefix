import pickle # pragma: no cover
import time # pragma: no cover

self = type('MockSelf', (object,), {})() # pragma: no cover
self._fingerprinter = type('MockFingerprinter', (object,), {'fingerprint': lambda self, request: b'deadbeef'})() # pragma: no cover
self.db = {'deadbeef_time': time.time() - 3600, 'deadbeef_data': pickle.dumps('Some data')} # pragma: no cover
self.expiration_secs = 7200 # pragma: no cover
request = None # pragma: no cover

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
