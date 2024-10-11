# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/988228/convert-a-string-representation-of-a-dictionary-to-a-dictionary
from l3.Runtime import _l_
try:
    import json
    _l_(13309)

except ImportError:
    pass
h = '{"foo":"bar", "foo2":"bar2"}'
_l_(13310)
d = json.loads(h)
_l_(13311)
d
_l_(13312)
{u'foo': u'bar', u'foo2': u'bar2'}
_l_(13313)
type(d)
_l_(13314)

