import time # pragma: no cover

blob = type('Mock', (object,), {'md5_hash': 'd41d8cd98f00b204e9800998ecf8427e', 'updated': type('Mock', (object,), {'timetuple': lambda: time.gmtime(0)})()})() # pragma: no cover

import time # pragma: no cover
from datetime import datetime # pragma: no cover

mock_updated = type('Mock', (object,), {'timetuple': lambda self: time.strptime('2023-10-01 12:00:00', '%Y-%m-%d %H:%M:%S')}) # pragma: no cover
blob = type('Mock', (object,), {'md5_hash': 'd41d8cd98f00b204e9800998ecf8427e', 'updated': mock_updated()})() # pragma: no cover

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
