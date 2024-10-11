import time # pragma: no cover
from datetime import datetime # pragma: no cover

blob = type('MockBlob', (object,), {'md5_hash': 'dummy_md5_hash', 'updated': datetime(2023, 1, 1, 12, 0, 0)})() # pragma: no cover
time = type('MockTime', (object,), {'mktime': time.mktime})() # pragma: no cover

import time # pragma: no cover
from datetime import datetime # pragma: no cover

class MockBlob:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.md5_hash = 'dummy_md5_hash'# pragma: no cover
        self.updated = datetime(2023, 10, 10, 12, 0, 0)# pragma: no cover
# pragma: no cover
blob = MockBlob() # pragma: no cover

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
