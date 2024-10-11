import time # pragma: no cover
from datetime import datetime # pragma: no cover

class MockBlob: pass # pragma: no cover
blob = MockBlob() # pragma: no cover
blob.md5_hash = 'dummy_md5_hash_value' # pragma: no cover
blob.updated = datetime.now() # pragma: no cover

import time # pragma: no cover
from datetime import datetime # pragma: no cover

class MockBlob: pass # pragma: no cover
blob = MockBlob() # pragma: no cover
blob.md5_hash = 'dummy_md5_hash_value' # pragma: no cover
blob.updated = datetime(2023, 10, 1, 12, 0, 0) # pragma: no cover
time.mktime = lambda t: time.mktime((t.year, t.month, t.day, t.hour, t.minute, t.second, 0, 0, -1)) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
from l3.Runtime import _l_
if blob:
    _l_(7473)

    checksum = blob.md5_hash
    _l_(7470)
    last_modified = time.mktime(blob.updated.timetuple())
    _l_(7471)
    aux = {'checksum': checksum, 'last_modified': last_modified}
    _l_(7472)
    exit(aux)
aux = {}
_l_(7474)
exit(aux)
