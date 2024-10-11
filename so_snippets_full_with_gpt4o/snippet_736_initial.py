# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2891790/pretty-print-a-numpy-array-without-scientific-notation-and-with-given-precision
from l3.Runtime import _l_
try:
    import numpy as np
    _l_(13825)

except ImportError:
    pass

x = np.random.random([5,5])
_l_(13826)
print(x.round(3))
_l_(13827)

