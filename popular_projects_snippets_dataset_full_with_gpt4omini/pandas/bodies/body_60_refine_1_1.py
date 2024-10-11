import pandas as pd # pragma: no cover
from pandas import Series # pragma: no cover

import pandas as pd # pragma: no cover
from pandas import Series # pragma: no cover

class MockTimestamp:  # Mock for pd.Timestamp# pragma: no cover
    def __init__(self, date_str):# pragma: no cover
        self.date = pd.to_datetime(date_str)# pragma: no cover
    @property# pragma: no cover
    def hour(self): return self.date.hour# pragma: no cover
    @property# pragma: no cover
    def day(self): return self.date.day# pragma: no cover
    @property# pragma: no cover
    def month(self): return self.date.month # pragma: no cover
class MockTimedelta:  # Mock for pd.Timedelta# pragma: no cover
    def __init__(self, days):# pragma: no cover
        self.days = days # pragma: no cover
class MockPandas:  # Mock for pd# pragma: no cover
    @staticmethod# pragma: no cover
    def date_range(start, periods):# pragma: no cover
        return [MockTimestamp(start) + MockTimedelta(i) for i in range(periods)]# pragma: no cover
    Timestamp = MockTimestamp# pragma: no cover
    Timedelta = MockTimedelta # pragma: no cover
pd = MockPandas() # pragma: no cover

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
