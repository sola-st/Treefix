from bz2 import BZ2File # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
file = 'example.bz2' # pragma: no cover
feed_options = {'bz2_compresslevel': 5} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/postprocessing.py
from l3.Runtime import _l_
self.file = file
_l_(6768)
self.feed_options = feed_options
_l_(6769)
compress_level = self.feed_options.get("bz2_compresslevel", 9)
_l_(6770)
self.bz2file = BZ2File(filename=self.file, mode="wb", compresslevel=compress_level)
_l_(6771)
