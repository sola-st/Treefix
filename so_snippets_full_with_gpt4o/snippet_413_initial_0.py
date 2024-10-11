values = [3, 2, 2, 5, 4] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2474015/getting-the-index-of-the-returned-max-or-min-item-using-max-min-on-a-list
from l3.Runtime import _l_
min_value = min(values)
_l_(13821)
indexes_with_min_value = [i for i in range(0,len(values)) if values[i] == min_value]
_l_(13822)

choosen = indexes_with_min_value[0]
_l_(13823)

