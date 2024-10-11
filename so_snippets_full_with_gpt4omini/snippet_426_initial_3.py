import pandas as pd # pragma: no cover

df = pd.DataFrame({'A': [1, 2, None], 'B': [None, 5, 6]}) # pragma: no cover
df.isnull = type('Mock', (object,), {'sum': lambda self: self._sum()})() # pragma: no cover
def _sum(self): return pd.Series({'A': 1, 'B': 1}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/29530232/how-to-check-if-any-value-is-nan-in-a-pandas-dataframe
from l3.Runtime import _l_
df.isnull().sum()
_l_(3214)

