import pandas as pd # pragma: no cover
from pandas import Series # pragma: no cover

import pandas as pd # pragma: no cover
from pandas import Series # pragma: no cover

class MockDateRange:# pragma: no cover
    def __init__(self, start, periods):# pragma: no cover
        self.dates = [pd.Timestamp(start) + pd.Timedelta(days=i) for i in range(periods)]# pragma: no cover
    def __getitem__(self, item):# pragma: no cover
        return self.dates[item]# pragma: no cover
    def __len__(self):# pragma: no cover
        return len(self.dates) # pragma: no cover
def date_range(start, periods):# pragma: no cover
    return MockDateRange(start, periods) # pragma: no cover
pd = type('Mock', (object,), {'date_range': staticmethod(date_range)})() # pragma: no cover

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
