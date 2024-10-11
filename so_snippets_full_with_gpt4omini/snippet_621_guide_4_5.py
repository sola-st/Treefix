import pandas as pd # pragma: no cover

df1 = pd.DataFrame({0: ['row1_col0', 'row2_col0', 'row3_col0'], 1: ['row1_col1', 'row2_col1', 'row3_col1'], 2: ['row1_col2', 'row2_col2', 'row3_col2'], 3: ['row1_col3', 'row2_col3', 'row3_col3']}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/14940743/selecting-excluding-sets-of-columns-in-pandas
from l3.Runtime import _l_
df2 = df1[['A','D']]
_l_(1605)

df2 = df1[[0,3]]
_l_(1606)

