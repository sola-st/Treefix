# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1653970/does-python-have-an-ordered-set
from l3.Runtime import _l_
keywords = ['foo', 'bar', 'bar', 'foo', 'baz', 'foo']
_l_(1669)

list(dict.fromkeys(keywords))
_l_(1670)
['foo', 'bar', 'baz']
_l_(1671)

