import pickle # pragma: no cover

class Mock(object):# pragma: no cover
    def __init__(self):# pragma: no cover
        self.file = open('dummy.pkl', 'wb')# pragma: no cover
        self.protocol = pickle.HIGHEST_PROTOCOL# pragma: no cover
# pragma: no cover
    def _get_serialized_fields(self, item):# pragma: no cover
        return {'key': 'value'}# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
item = 'dummy_item' # pragma: no cover
pickle = pickle # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/exporters.py
from l3.Runtime import _l_
d = dict(self._get_serialized_fields(item))
_l_(17434)
pickle.dump(d, self.file, self.protocol)
_l_(17435)
