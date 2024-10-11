import bz2 # pragma: no cover

data = b'This is some binary data.' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/postprocessing.py
from l3.Runtime import _l_
aux = self.bz2file.write(data)
_l_(9349)
exit(aux)
