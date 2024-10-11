import pandas as pd # pragma: no cover
from pandas import Series # pragma: no cover

import pandas as pd # pragma: no cover
from pandas import Series # pragma: no cover

type('MockDatetime', (object,), {'hour': 1, 'day': 1, 'month': 1}) # pragma: no cover
ser = Series([pd.Timestamp('2000-01-01 01:00:00') for _ in range(10)]) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
# GH#2689, GH#2627
from l3.Runtime import _l_
ser = Series(pd.date_range("1/1/2000", periods=10))
_l_(21077)

def func(x):
    _l_(21079)

    aux = (x.hour, x.day, x.month)
    _l_(21078)
    exit(aux)

# it works!
ser.map(func)
_l_(21080)
ser.apply(func)
_l_(21081)
