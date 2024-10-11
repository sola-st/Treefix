mydict = {'foo1': 1, 'foo2': 2, 'bar1': 3, 'baz': 4} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3420122/filter-dict-to-contain-only-certain-keys
from l3.Runtime import _l_
foodict = {k: v for k, v in mydict.items() if k.startswith('foo')}
_l_(2569)

