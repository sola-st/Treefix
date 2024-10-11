import collections # pragma: no cover
try:# pragma: no cover
    import ordereddict# pragma: no cover
except ImportError:# pragma: no cover
    pass # pragma: no cover

json_str = '{"key": "value"}' # pragma: no cover
json = type('Mock', (object,), {'loads': lambda x, object_pairs_hook: collections.OrderedDict([('key', 'value')])}) # pragma: no cover

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

