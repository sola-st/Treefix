import pandas as pd # pragma: no cover

df1 = pd.DataFrame({# pragma: no cover
    'A': [1, 2, 3],# pragma: no cover
    'B': [4, 5, 6],# pragma: no cover
    'C': [7, 8, 9],# pragma: no cover
    'D': [10, 11, 12]# pragma: no cover
}) # pragma: no cover

import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

df1 = pd.DataFrame(np.random.randn(5, 4), columns=list('ABCD')) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/14940743/selecting-excluding-sets-of-columns-in-pandas
from l3.Runtime import _l_
df2 = df1[['A','D']]
_l_(13794)

df2 = df1[[0,3]]
_l_(13795)

