import pandas as pd # pragma: no cover

Series = pd.Series # pragma: no cover
x = {'value': pd.Series([1, 2, 3])} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_timegrouper.py
from l3.Runtime import _l_
aux = Series([x["value"].sum()], ("sum",))
_l_(20864)
exit(aux)
