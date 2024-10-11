class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.prefix = 'Prefix: ' # pragma: no cover
path = '/some/path' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
from l3.Runtime import _l_
aux = self.prefix + path
_l_(8884)
exit(aux)
