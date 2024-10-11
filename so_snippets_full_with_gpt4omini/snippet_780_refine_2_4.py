import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

iris1 = pd.DataFrame(np.random.rand(10, 4)) # pragma: no cover
iris2 = pd.DataFrame(np.random.rand(10, 4)) # pragma: no cover
array1 = np.array([1, 2, 3]) # pragma: no cover
array2 = np.array([1, 2, 3]) # pragma: no cover
identical = lambda x, y: np.array_equal(x, y) # pragma: no cover

import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

iris1 = pd.DataFrame(np.array([[5.1, 3.5, 1.4, 0.2], [4.9, 3.0, 1.4, 0.2]])) # pragma: no cover
iris2 = pd.DataFrame(np.array([[5.1, 3.5, 1.4, 0.2], [4.9, 3.0, 1.4, 0.2]])) # pragma: no cover
array1 = np.array([1, 2, 3]) # pragma: no cover
array2 = np.array([1, 2, 3]) # pragma: no cover
all_equal = lambda x, y: np.array_equal(x, y) # pragma: no cover

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

