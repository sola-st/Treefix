from io import BytesIO # pragma: no cover

self = type('Mock', (object,), {'indent': 2, 'file': BytesIO()})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/exporters.py
from l3.Runtime import _l_
if self.indent is not None:
    _l_(6005)

    self.file.write(b'\n')
    _l_(6004)
