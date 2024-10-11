# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4260280/if-else-in-a-list-comprehension
from l3.Runtime import _l_
xs = [None, 'This', 'is', 'a', 'filler', 'test', 'string', None]
_l_(13174)

d = {None: '', 'filler': 'manipulated'}
_l_(13175)

res = [d.get(x, x) for x in xs]
_l_(13176)

print(res)
_l_(13177)

['', 'This', 'is', 'a', 'manipulated', 'test', 'string', '']
_l_(13178)

