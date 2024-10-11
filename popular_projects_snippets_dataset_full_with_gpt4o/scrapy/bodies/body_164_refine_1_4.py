import time # pragma: no cover
import datetime # pragma: no cover

blob = type('Mock', (object,), {# pragma: no cover
  'md5_hash': 'd41d8cd98f00b204e9800998ecf8427e',# pragma: no cover
  'updated': datetime.datetime(2023, 1, 1, 12, 0, 0)# pragma: no cover
})() # pragma: no cover

import time # pragma: no cover
from datetime import datetime # pragma: no cover

blob = type('Mock', (object,), {# pragma: no cover
  'md5_hash': 'd41d8cd98f00b204e9800998ecf8427e',# pragma: no cover
  'updated': datetime(2023, 10, 10, 10, 10, 10)# pragma: no cover
})() # pragma: no cover

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
