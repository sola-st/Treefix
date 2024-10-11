from pathlib import Path # pragma: no cover
import types # pragma: no cover

self = types.SimpleNamespace() # pragma: no cover
self.jobdir = '/some/directory/path' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/spiderstate.py
from l3.Runtime import _l_
aux = str(Path(self.jobdir, 'spider.state'))
_l_(16478)
exit(aux)
