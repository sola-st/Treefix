import io # pragma: no cover

file = io.StringIO('some initial text data needed to create the file-like object') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
from l3.Runtime import _l_
file.close()
_l_(20919)
