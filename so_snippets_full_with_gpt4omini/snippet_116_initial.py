# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4260280/if-else-in-a-list-comprehension
from l3.Runtime import _l_
xs = [None, 'This', 'is', 'a', 'filler', 'test', 'string', None]
_l_(1556)

d = {None: '', 'filler': 'manipulated'}
_l_(1557)

res = [d.get(x, x) for x in xs]
_l_(1558)

print(res)
_l_(1559)

['', 'This', 'is', 'a', 'manipulated', 'test', 'string', '']
_l_(1560)

