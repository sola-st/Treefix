import time # pragma: no cover
import pickle # pragma: no cover

request = 'mock_request' # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
self._fingerprinter = type('Mock', (object,), {'fingerprint': lambda self, req: b'1234abcd'})() # pragma: no cover
self.db = {'5678abcd_time': str(time.time() - 1000), '5678abcd_data': pickle.dumps('mock_data')} # pragma: no cover
self.expiration_secs = 2000 # pragma: no cover

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
