# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/7604966/maximum-and-minimum-values-for-ints
from l3.Runtime import _l_
try:
    import sys
    _l_(3303)

except ImportError:
    pass
max_size = sys.maxsize
_l_(3304)
min_size = -sys.maxsize - 1
_l_(3305)

