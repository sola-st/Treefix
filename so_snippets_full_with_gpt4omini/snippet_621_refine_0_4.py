import pandas as pd # pragma: no cover

df1 = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8], 'C': [9, 10, 11, 12], 'D': [13, 14, 15, 16]}) # pragma: no cover

import pandas as pd # pragma: no cover

df1 = pd.DataFrame({'A': [10, 20, 30, 40], 'B': [50, 60, 70, 80], 'C': [90, 100, 110, 120], 'D': [130, 140, 150, 160]}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/14940743/selecting-excluding-sets-of-columns-in-pandas
from l3.Runtime import _l_
df2 = df1[['A','D']]
_l_(1605)

df2 = df1[[0,3]]
_l_(1606)

