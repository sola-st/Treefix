import pandas as pd # pragma: no cover
from pandas import Series # pragma: no cover

import pandas as pd # pragma: no cover
from pandas import Series # pragma: no cover

class MockTimestamp:  # Mock class to simulate pd.Timestamp # pragma: no cover
    def __init__(self, date_str): # pragma: no cover
        self.timestamp = pd.to_datetime(date_str) # pragma: no cover
    @property # pragma: no cover
    def hour(self): return self.timestamp.hour # pragma: no cover
    @property # pragma: no cover
    def day(self): return self.timestamp.day # pragma: no cover
    @property # pragma: no cover
    def month(self): return self.timestamp.month # pragma: no cover
class MockTimedelta: # pragma: no cover
    @staticmethod # pragma: no cover
    def days(days): return pd.Timedelta(days=days) # pragma: no cover
pd = type('Mock', (object,), { # pragma: no cover
    'date_range': staticmethod(lambda start, periods: [MockTimestamp(start) + MockTimedelta.days(i) for i in range(periods)]) # pragma: no cover
})() # pragma: no cover

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
