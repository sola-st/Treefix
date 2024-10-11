import pandas as pd # pragma: no cover

Series = pd.Series # pragma: no cover
x = pd.DataFrame({'value': [10, 20, 30]}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_timegrouper.py
from l3.Runtime import _l_
aux = Series([x["value"].sum()], ("sum",))
_l_(10118)
exit(aux)
