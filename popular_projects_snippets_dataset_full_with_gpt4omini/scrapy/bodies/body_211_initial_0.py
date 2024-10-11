from pathlib import Path # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.jobdir = '/mock/directory' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/spiderstate.py
from l3.Runtime import _l_
aux = str(Path(self.jobdir, 'spider.state'))
_l_(5438)
exit(aux)
