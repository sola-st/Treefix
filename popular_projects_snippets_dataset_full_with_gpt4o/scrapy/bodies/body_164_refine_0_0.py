import time # pragma: no cover
from datetime import datetime # pragma: no cover

blob = type('Mock', (object,), {'md5_hash': 'fake_md5_hash', 'updated': datetime.now()})() # pragma: no cover

import time # pragma: no cover
from datetime import datetime # pragma: no cover

class MockBlob(object): # pragma: no cover
    md5_hash = 'fake_md5_hash' # pragma: no cover
    updated = datetime(2022, 8, 27, 14, 40, 15) # pragma: no cover
blob = MockBlob() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
from l3.Runtime import _l_
if blob:
    _l_(18337)

    checksum = blob.md5_hash
    _l_(18334)
    last_modified = time.mktime(blob.updated.timetuple())
    _l_(18335)
    aux = {'checksum': checksum, 'last_modified': last_modified}
    _l_(18336)
    exit(aux)
aux = {}
_l_(18338)
exit(aux)
