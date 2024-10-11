import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover

df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/26414913/normalize-columns-of-a-dataframe
from l3.Runtime import _l_
df = df/df.max().astype(np.float64)
_l_(12595)

df = df/df.loc[df.abs().idxmax()].astype(np.float64)
_l_(12596)

