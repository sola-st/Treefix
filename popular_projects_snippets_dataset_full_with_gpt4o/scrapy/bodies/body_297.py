# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/postprocessing.py
from l3.Runtime import _l_
prev = self.file
_l_(18666)
for plugin in self.plugins[::-1]:
    _l_(18668)

    prev = plugin(prev, self.feed_options)
    _l_(18667)
aux = prev
_l_(18669)
exit(aux)
