import time # pragma: no cover
class MockBlob: pass # pragma: no cover

blob = MockBlob() # pragma: no cover
blob.md5_hash = 'dummy_checksum' # pragma: no cover
blob.updated = datetime.now() # pragma: no cover

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
