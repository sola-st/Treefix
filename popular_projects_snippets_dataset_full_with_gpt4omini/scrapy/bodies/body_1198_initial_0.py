from scrapy.selector import Selector # pragma: no cover

query = 'div.classname' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/response/text.py
from l3.Runtime import _l_
aux = self.selector.css(query)
_l_(9540)
exit(aux)
