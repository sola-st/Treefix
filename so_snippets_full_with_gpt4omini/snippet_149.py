# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
from l3.Runtime import _l_
stats = {'a':1000, 'b':3000, 'c': 100, 'd':3000, 'e':3000}
_l_(1564)
try:
    from collections import defaultdict
    _l_(1566)

except ImportError:
    pass
try:
    from collections import OrderedDict
    _l_(1568)

except ImportError:
    pass

groupedByValue = defaultdict(list)
_l_(1569)
for key, value in sorted(stats.items()):
    _l_(1571)

    groupedByValue[value].append(key)
    _l_(1570)

# {1000: ['a'], 3000: ['b', 'd', 'e'], 100: ['c']}

groupedByValue[max(groupedByValue)]
_l_(1572)
# ['b', 'd', 'e']

