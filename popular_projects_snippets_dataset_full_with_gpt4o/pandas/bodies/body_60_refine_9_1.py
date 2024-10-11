import pandas as pd # pragma: no cover
from pandas import Series # pragma: no cover

import pandas as pd # pragma: no cover
from pandas import Series # pragma: no cover

series_data = [pd.Timestamp('2000-01-01'), pd.Timestamp('2000-01-02'), pd.Timestamp('2000-01-03'), pd.Timestamp('2000-01-04'), pd.Timestamp('2000-01-05'), pd.Timestamp('2000-01-06'), pd.Timestamp('2000-01-07'), pd.Timestamp('2000-01-08'), pd.Timestamp('2000-01-09'), pd.Timestamp('2000-01-10')] # pragma: no cover
ser = Series(series_data) # pragma: no cover

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
