import pandas as pd # pragma: no cover
from pandas import Series # pragma: no cover

ser = Series(pd.date_range('1/1/2000', periods=10)) # pragma: no cover
setattr(pd.Timestamp, 'hour', property(lambda self: self.to_pydatetime().hour)) # pragma: no cover
setattr(pd.Timestamp, 'day', property(lambda self: self.to_pydatetime().day)) # pragma: no cover
setattr(pd.Timestamp, 'month', property(lambda self: self.to_pydatetime().month)) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
# GH#2689, GH#2627
from l3.Runtime import _l_
ser = Series(pd.date_range("1/1/2000", periods=10))
_l_(10142)

def func(x):
    _l_(10144)

    aux = (x.hour, x.day, x.month)
    _l_(10143)
    exit(aux)

# it works!
ser.map(func)
_l_(10145)
ser.apply(func)
_l_(10146)
