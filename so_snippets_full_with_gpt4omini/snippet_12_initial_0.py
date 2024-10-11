a = list(range(10)) # pragma: no cover
start = 0 # pragma: no cover
end = 10 # pragma: no cover
step = 1 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/509211/understanding-slicing
from l3.Runtime import _l_
a[start:end:step]
_l_(1600)
# for(i = start; i < end; i += step)

