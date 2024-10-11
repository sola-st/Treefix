import json # pragma: no cover
import collections # pragma: no cover
import simplejson as json # pragma: no cover

json_str = '[["key1", "value1"], ["key2", "value2"]]' # pragma: no cover
collections = type('Mock', (object,), {'OrderedDict': collections.OrderedDict}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6921699/can-i-get-json-to-load-into-an-ordereddict
from l3.Runtime import _l_
my_ordered_dict = json.loads(json_str, object_pairs_hook=collections.OrderedDict)
_l_(596)
try:
    import simplejson as json
    _l_(598)

except ImportError:
    pass
try:
    import ordereddict
    _l_(600)

except ImportError:
    pass

my_ordered_dict = json.loads(json_str, object_pairs_hook=ordereddict.OrderedDict)
_l_(601)

