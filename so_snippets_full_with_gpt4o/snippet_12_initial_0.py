a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # pragma: no cover
start = 0 # pragma: no cover
end = 10 # pragma: no cover
step = 2 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/509211/understanding-slicing
from l3.Runtime import _l_
a[start:end:step]
_l_(13642)
# for(i = start; i < end; i += step)

