import pickle # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.file = open('output.pkl', 'wb') # pragma: no cover
self.protocol = pickle.HIGHEST_PROTOCOL # pragma: no cover
def _get_serialized_fields(item): return {'key': item} # pragma: no cover
self._get_serialized_fields = _get_serialized_fields # pragma: no cover
item = 'value' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/exporters.py
from l3.Runtime import _l_
d = dict(self._get_serialized_fields(item))
_l_(6002)
pickle.dump(d, self.file, self.protocol)
_l_(6003)
