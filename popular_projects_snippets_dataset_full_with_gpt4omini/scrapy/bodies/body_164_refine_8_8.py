import time # pragma: no cover
from unittest.mock import MagicMock # pragma: no cover

blob = MagicMock() # pragma: no cover
blob.md5_hash = 'abc123' # pragma: no cover
blob.updated = time.strptime('2023-10-03 15:00:00', '%Y-%m-%d %H:%M:%S') # pragma: no cover

import time # pragma: no cover
from datetime import datetime # pragma: no cover

class MockBlob:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.md5_hash = 'abc123'# pragma: no cover
        self.updated = datetime(2023, 10, 3, 15, 0, 0)# pragma: no cover
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
