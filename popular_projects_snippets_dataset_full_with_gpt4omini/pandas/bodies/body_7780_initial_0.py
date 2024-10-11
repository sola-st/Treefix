import pandas as pd # pragma: no cover

date_range = pd.date_range # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike_/test_equals.py
from l3.Runtime import _l_
aux = date_range("2013-01-01", periods=5)
_l_(10638)
exit(aux)
