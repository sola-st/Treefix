import bz2 # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
self.bz2file = bz2.BZ2File('/tmp/dummyfile.bz2', 'w') # pragma: no cover
data = b'Some binary data to compress' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/postprocessing.py
from l3.Runtime import _l_
aux = self.bz2file.write(data)
_l_(20422)
exit(aux)
