import time # pragma: no cover
from datetime import datetime # pragma: no cover
class MockBlob: # pragma: no cover
    def __init__(self, md5_hash, updated): # pragma: no cover
        self.md5_hash = md5_hash # pragma: no cover
        self.updated = updated # pragma: no cover
    def timetuple(self): # pragma: no cover
        return self.updated.timetuple() # pragma: no cover

blob = MockBlob('sample_md5', datetime(2023, 10, 1, 12, 0, 0)) # pragma: no cover

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
