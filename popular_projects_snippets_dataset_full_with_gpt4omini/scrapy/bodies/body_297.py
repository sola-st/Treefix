# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/postprocessing.py
from l3.Runtime import _l_
prev = self.file
_l_(7820)
for plugin in self.plugins[::-1]:
    _l_(7822)

    prev = plugin(prev, self.feed_options)
    _l_(7821)
aux = prev
_l_(7823)
exit(aux)
