result = 0 # pragma: no cover
d = type('Mock', (object,), {'callback': lambda self, x: print(f'Callback called with result: {x}')})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/robotstxt.py
from l3.Runtime import _l_
d.callback(result)
_l_(19978)
aux = result
_l_(19979)
exit(aux)
