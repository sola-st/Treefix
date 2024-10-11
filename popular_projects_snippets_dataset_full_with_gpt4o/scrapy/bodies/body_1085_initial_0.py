import json # pragma: no cover

args = {} # pragma: no cover
self = type('Mock', (object,), {'args': ['{"key": "value"}']})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/contracts/default.py
from l3.Runtime import _l_
args['cb_kwargs'] = json.loads(' '.join(self.args))
_l_(19423)
aux = args
_l_(19424)
exit(aux)
