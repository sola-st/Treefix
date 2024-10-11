import pandas as pd # pragma: no cover

df = pd.DataFrame({'A': range(10), 'B': range(10, 20)}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/16096627/selecting-a-row-of-pandas-series-dataframe-by-integer-index
from l3.Runtime import _l_
df[2:3]
_l_(14535)

df[6:20:3]
_l_(14536)

