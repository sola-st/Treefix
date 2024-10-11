import pandas as pd # pragma: no cover
from pandas import DateOffset # pragma: no cover

df = pd.DataFrame({'date': pd.date_range(start='2023-01-01', periods=10, freq='D')}) # pragma: no cover
df.first = lambda offset: df.iloc[0:1] if offset == 'd' else df.iloc[0:3]  # Mock implementation of first method # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/25254016/get-first-row-value-of-a-given-column
from l3.Runtime import _l_
x = df.first('d') # Returns the first day. '3d' gives first three days.
_l_(1735) # Returns the first day. '3d' gives first three days.

