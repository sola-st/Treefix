import pandas as pd # pragma: no cover
from pandas import TimedeltaIndex # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_delete.py
# GH#30655 behavior matches DatetimeIndex

from l3.Runtime import _l_
tdi = TimedeltaIndex(["1 Day", "2 Days", None, "3 Days", "4 Days"])
_l_(6524)
result = tdi.delete(2)
_l_(6525)
assert result.freq is None
_l_(6526)
