import pandas as pd # pragma: no cover
from pandas.io.formats.style import Styler # pragma: no cover

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}) # pragma: no cover
Styler = type('MockStyler', (object,), {'__init__': lambda self, df, uuid_len: None}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_exceptions.py
from l3.Runtime import _l_
aux = Styler(df, uuid_len=0)
_l_(7070)
exit(aux)
