import pandas as pd # pragma: no cover

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}) # pragma: no cover
def has_horizontally_truncated_repr(df): return df.shape[1] > 1 # pragma: no cover
def has_vertically_truncated_repr(df): return df.shape[0] > 2 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
from l3.Runtime import _l_
aux = has_horizontally_truncated_repr(df) and has_vertically_truncated_repr(df)
_l_(10852)
exit(aux)
