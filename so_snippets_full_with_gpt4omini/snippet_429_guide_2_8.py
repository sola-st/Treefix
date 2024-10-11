from itertools import groupby # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/773/how-do-i-use-itertools-groupby
from l3.Runtime import _l_
for x in list(groupby(range(10))):
    _l_(1840)

    print(list(x[1]))
    _l_(1839)

[]
_l_(1841)
[]
_l_(1842)
[]
_l_(1843)
[]
_l_(1844)
[]
_l_(1845)
[]
_l_(1846)
[]
_l_(1847)
[]
_l_(1848)
[]
_l_(1849)
[9]
_l_(1850)

def groupbylist(*args, **kwargs):
    _l_(1852)

    aux = [(k, list(g)) for k, g in groupby(*args, **kwargs)]
    _l_(1851)
    return aux

