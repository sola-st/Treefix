import pandas as pd # pragma: no cover
from pandas import Series # pragma: no cover

ser = Series(pd.date_range('1/1/2000', periods=10)) # pragma: no cover
class MockTimestamp: # pragma: no cover
    def __init__(self, date): # pragma: no cover
        self.date = date # pragma: no cover
    @property # pragma: no cover
    def hour(self): return self.date.hour # pragma: no cover
    @property # pragma: no cover
    def day(self): return self.date.day # pragma: no cover
    @property # pragma: no cover
    def month(self): return self.date.month # pragma: no cover
pd.Timestamp = MockTimestamp # pragma: no cover
setattr(Series, '__getitem__', lambda self, idx: MockTimestamp(self[idx])) # pragma: no cover

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
