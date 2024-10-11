import simplejson as json # pragma: no cover
import collections # pragma: no cover

json_str = '{"key1": "value1", "key2": "value2"}' # pragma: no cover
collections.OrderedDict = type('Mock', (object,), {}) # pragma: no cover

import simplejson as json # pragma: no cover
import collections # pragma: no cover

json_str = '{"key1": "value1", "key2": "value2"}' # pragma: no cover
class MockOrderedDict(dict): # pragma: no cover
    def __init__(self, *args, **kwargs): # pragma: no cover
        super(MockOrderedDict, self).__init__(*args, **kwargs) # pragma: no cover
collections.OrderedDict = MockOrderedDict # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6921699/can-i-get-json-to-load-into-an-ordereddict
from l3.Runtime import _l_
my_ordered_dict = json.loads(json_str, object_pairs_hook=collections.OrderedDict)
_l_(12589)
try:
    import simplejson as json
    _l_(12591)

except ImportError:
    pass
try:
    import ordereddict
    _l_(12593)

except ImportError:
    pass

my_ordered_dict = json.loads(json_str, object_pairs_hook=ordereddict.OrderedDict)
_l_(12594)

