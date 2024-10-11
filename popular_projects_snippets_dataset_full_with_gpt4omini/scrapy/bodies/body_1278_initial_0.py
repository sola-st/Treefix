from unittest.mock import Mock # pragma: no cover

d = Mock() # pragma: no cover
result = 42 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/robotstxt.py
from l3.Runtime import _l_
d.callback(result)
_l_(8885)
aux = result
_l_(8886)
exit(aux)
