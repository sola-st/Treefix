import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

def identical(df1, df2): return df1.equals(df2) # pragma: no cover
iris1 = pd.DataFrame(np.random.rand(150, 5), columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']) # pragma: no cover
iris2 = iris1.copy() # pragma: no cover
array1 = np.arange(0.0, 10.2, 0.12) # pragma: no cover
array2 = np.arange(0.0, 10.2, 0.12) # pragma: no cover

import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

def identical(df1, df2): return df1.equals(df2) # pragma: no cover
iris1 = pd.DataFrame(np.random.rand(150, 5), columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']) # pragma: no cover
iris2 = iris1.copy() # pragma: no cover
array1 = np.arange(0.0, 10.2, 0.12) # pragma: no cover
array2 = np.arange(0.0, 10.2, 0.12) # pragma: no cover
def all_equal(arr1, arr2): return np.array_equal(arr1, arr2) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/10580676/comparing-two-numpy-arrays-for-equality-element-wise
from l3.Runtime import _l_
try:
    import numpy as np
    _l_(13977)

except ImportError:
    pass
a = np.arange(0.0, 10.2, 0.12)
_l_(13978)
b = np.arange(0.0, 10.2, 0.12)
_l_(13979)
ap = pd.DataFrame(a)
_l_(13980)
bp = pd.DataFrame(b)
_l_(13981)

ap.equals(bp)
_l_(13982)
True
_l_(13983)

identical(iris1, iris2)
_l_(13984)
#[1] TRUE
all.equal(array1, array2)
_l_(13985)
#> [1] TRUE 

