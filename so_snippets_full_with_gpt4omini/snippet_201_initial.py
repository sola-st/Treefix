# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/988228/convert-a-string-representation-of-a-dictionary-to-a-dictionary
from l3.Runtime import _l_
try:
    import json
    _l_(1644)

except ImportError:
    pass
h = '{"foo":"bar", "foo2":"bar2"}'
_l_(1645)
d = json.loads(h)
_l_(1646)
d
_l_(1647)
{u'foo': u'bar', u'foo2': u'bar2'}
_l_(1648)
type(d)
_l_(1649)

