import json # pragma: no cover
class Mock: # pragma: no cover
    def __init__(self, args): # pragma: no cover
        self.args = args # pragma: no cover

args = {} # pragma: no cover
self = Mock(['{"key": "value"}']) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/contracts/default.py
from l3.Runtime import _l_
args['cb_kwargs'] = json.loads(' '.join(self.args))
_l_(8219)
aux = args
_l_(8220)
exit(aux)
