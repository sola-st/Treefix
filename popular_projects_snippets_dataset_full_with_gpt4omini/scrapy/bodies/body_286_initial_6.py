import bz2 # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.bz2file = bz2.BZ2File('example.bz2', 'wb') # pragma: no cover
data = b'This is an example of data to be written in compressed format.' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/postprocessing.py
from l3.Runtime import _l_
aux = self.bz2file.write(data)
_l_(9349)
exit(aux)
