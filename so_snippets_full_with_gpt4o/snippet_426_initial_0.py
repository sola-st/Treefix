import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

data = {'A': [1, 2, np.nan], 'B': [4, np.nan, 6], 'C': [7, 8, 9]} # pragma: no cover
df = pd.DataFrame(data) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/29530232/how-to-check-if-any-value-is-nan-in-a-pandas-dataframe
from l3.Runtime import _l_
df.isnull().sum()
_l_(15270)

