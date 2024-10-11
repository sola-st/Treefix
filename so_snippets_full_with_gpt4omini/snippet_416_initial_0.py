import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover

df = pd.DataFrame([[np.nan, 0.2, np.nan], [np.nan, np.nan, 0.5], [np.nan, 0.2, 0.5], [0.1, 0.2, np.nan], [0.1, 0.2, 0.5], [0.1, np.nan, 0.5], [0.1, np.nan, np.nan]]) # pragma: no cover
array = np.array # pragma: no cover
nan = np.nan # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/13187778/convert-pandas-dataframe-to-numpy-array
from l3.Runtime import _l_
df.values
_l_(568)

array([[nan, 0.2, nan],
       [nan, nan, 0.5],
       [nan, 0.2, 0.5],
       [0.1, 0.2, nan],
       [0.1, 0.2, 0.5],
       [0.1, nan, 0.5],
       [0.1, nan, nan]])
_l_(569)

