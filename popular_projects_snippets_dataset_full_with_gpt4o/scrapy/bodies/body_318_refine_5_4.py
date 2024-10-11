import time # pragma: no cover
import pickle # pragma: no cover

import time # pragma: no cover
import pickle # pragma: no cover
from datetime import datetime # pragma: no cover

class MockFingerprinter:# pragma: no cover
    def fingerprint(self, request):# pragma: no cover
        return b'test_key' # pragma: no cover
class MockDB(dict):# pragma: no cover
    pass # pragma: no cover
class MockSelf:# pragma: no cover
    def __init__(self):# pragma: no cover
        self._fingerprinter = MockFingerprinter()# pragma: no cover
        self.db = MockDB()# pragma: no cover
        self.expiration_secs = 3600 # pragma: no cover
self = MockSelf()# pragma: no cover
self.db['test_key_time'] = str(time.time())# pragma: no cover
self.db['test_key_data'] = pickle.dumps({'data': 'test_data'}) # pragma: no cover
request = {} # pragma: no cover
time = datetime.now().timestamp # pragma: no cover

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
