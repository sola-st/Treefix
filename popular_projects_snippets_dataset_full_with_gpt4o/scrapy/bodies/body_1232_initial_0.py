import io # pragma: no cover

self = type("Mock", (object,), {})() # pragma: no cover
self.indent = 4 # pragma: no cover
self.file = io.BytesIO() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/exporters.py
from l3.Runtime import _l_
if self.indent is not None:
    _l_(17437)

    self.file.write(b'\n')
    _l_(17436)
