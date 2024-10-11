import pandas as pd # pragma: no cover
import uuid # pragma: no cover

df = pd.DataFrame({'A': range(5), 'B': range(5, 10)}) # pragma: no cover
Styler = type('MockStyler', (object,), {'__init__': lambda self, df, uuid_len: None}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_exceptions.py
from l3.Runtime import _l_
aux = Styler(df, uuid_len=0)
_l_(19472)
exit(aux)
