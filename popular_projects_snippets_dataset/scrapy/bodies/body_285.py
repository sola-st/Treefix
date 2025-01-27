# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/postprocessing.py
from l3.Runtime import _l_
self.file = file
_l_(17523)
self.feed_options = feed_options
_l_(17524)
compress_level = self.feed_options.get("bz2_compresslevel", 9)
_l_(17525)
self.bz2file = BZ2File(filename=self.file, mode="wb", compresslevel=compress_level)
_l_(17526)
