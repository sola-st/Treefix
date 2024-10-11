import time # pragma: no cover
import pickle # pragma: no cover

class FingerprinterMock:# pragma: no cover
    def fingerprint(self, request):# pragma: no cover
        return b'example_fingerprint'# pragma: no cover
# pragma: no cover
class Mock:# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
request = 'example_request' # pragma: no cover
time = time.time # pragma: no cover
pickle.loads = lambda x: 'unpickled_data' # pragma: no cover
self._fingerprinter = FingerprinterMock() # pragma: no cover
self.db = {'example_fingerprint_time': time() - 1000, 'example_fingerprint_data': pickle.dumps('example_data')} # pragma: no cover
self.expiration_secs = 3600 # pragma: no cover

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
