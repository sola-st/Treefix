import pandas as pd # pragma: no cover

df1 = pd.DataFrame({0: [1, 2, 3], 1: ['A', 'B', 'C'], 2: [4, 5, 6], 3: ['D', 'E', 'F']}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/14940743/selecting-excluding-sets-of-columns-in-pandas
from l3.Runtime import _l_
df2 = df1[['A','D']]
_l_(1605)

df2 = df1[[0,3]]
_l_(1606)

