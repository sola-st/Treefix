import pandas as pd # pragma: no cover
from pandas import Series # pragma: no cover

import pandas as pd # pragma: no cover
from pandas import Series # pragma: no cover

class MockTimestamp:# pragma: no cover
    def __init__(self, start):# pragma: no cover
        self._datetime = pd.to_datetime(start)# pragma: no cover
    @property# pragma: no cover
    def hour(self):# pragma: no cover
        return self._datetime.hour# pragma: no cover
    @property# pragma: no cover
    def day(self):# pragma: no cover
        return self._datetime.day# pragma: no cover
    @property# pragma: no cover
    def month(self):# pragma: no cover
        return self._datetime.month# pragma: no cover
# pragma: no cover
class MockDateRange:# pragma: no cover
    @staticmethod# pragma: no cover
    def date_range(start, periods):# pragma: no cover
        return [MockTimestamp(start) for _ in range(periods)]# pragma: no cover
# pragma: no cover
pd = type('Mock', (object,), {'date_range': MockDateRange.date_range, 'Timestamp': MockTimestamp})() # pragma: no cover

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
