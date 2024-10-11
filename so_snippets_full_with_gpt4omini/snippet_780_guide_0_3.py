import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

a = np.arange(0.0, 10.2, 0.12) # pragma: no cover
b = np.arange(0.0, 10.2, 0.12) # pragma: no cover
iris1 = pd.DataFrame(a) # pragma: no cover
iris2 = pd.DataFrame(b) # pragma: no cover
array1 = np.array(a) # pragma: no cover
array2 = np.array(b) # pragma: no cover
identical = type('Mock', (object,), {'__call__': lambda self, x, y: pd.DataFrame.equals(x, y)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/10580676/comparing-two-numpy-arrays-for-equality-element-wise
from l3.Runtime import _l_
try:
    import numpy as np
    _l_(1830)

except ImportError:
    pass
a = np.arange(0.0, 10.2, 0.12)
_l_(1831)
b = np.arange(0.0, 10.2, 0.12)
_l_(1832)
ap = pd.DataFrame(a)
_l_(1833)
bp = pd.DataFrame(b)
_l_(1834)

ap.equals(bp)
_l_(1835)
True
_l_(1836)

identical(iris1, iris2)
_l_(1837)
#[1] TRUE
all.equal(array1, array2)
_l_(1838)
#> [1] TRUE 

