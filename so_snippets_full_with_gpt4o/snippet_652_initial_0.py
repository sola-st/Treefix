import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

df = pd.DataFrame(np.random.randn(5, 3), columns=['B', 'A', 'C']) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/11067027/sorting-columns-in-pandas-dataframe-based-on-column-name
from l3.Runtime import _l_
df.sort_index(axis=1, inplace=True)
_l_(14691)

