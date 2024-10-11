import pandas as pd # pragma: no cover
from pandas import Series # pragma: no cover

import pandas as pd # pragma: no cover
from pandas import Series # pragma: no cover

class MockTimestamp: # pragma: no cover
    def __init__(self, date): # pragma: no cover
        self.date = pd.to_datetime(date) # pragma: no cover
        self.hour = self.date.hour # pragma: no cover
        self.day = self.date.day # pragma: no cover
        self.month = self.date.month # pragma: no cover
class MockTimedelta: # pragma: no cover
    def __init__(self, days): # pragma: no cover
        self.days = days # pragma: no cover
class Mock: # pragma: no cover
    Timestamp = MockTimestamp # pragma: no cover
    Timedelta = MockTimedelta # pragma: no cover
    @staticmethod # pragma: no cover
    def date_range(start, periods): # pragma: no cover
        return [pd.to_datetime(start) + pd.Timedelta(days=i) for i in range(periods)] # pragma: no cover
pd = Mock # pragma: no cover

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
