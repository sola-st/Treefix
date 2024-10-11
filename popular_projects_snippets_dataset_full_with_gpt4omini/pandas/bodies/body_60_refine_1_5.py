import pandas as pd # pragma: no cover
from pandas import Series # pragma: no cover

import pandas as pd # pragma: no cover
from pandas import Series # pragma: no cover

class MockTimestamp:# pragma: no cover
    def __init__(self, start):# pragma: no cover
        self.start = pd.to_datetime(start)# pragma: no cover
    @property# pragma: no cover
    def hour(self):# pragma: no cover
        return self.start.hour# pragma: no cover
    @property# pragma: no cover
    def day(self):# pragma: no cover
        return self.start.day# pragma: no cover
    @property# pragma: no cover
    def month(self):# pragma: no cover
        return self.start.month# pragma: no cover
# pragma: no cover
class Mock(pd.Series):# pragma: no cover
    @staticmethod# pragma: no cover
    def date_range(start, periods):# pragma: no cover
        return [MockTimestamp(start) + pd.Timedelta(days=i) for i in range(periods)]# pragma: no cover
# pragma: no cover
pd = type('MockPD', (object,), {'date_range': staticmethod(Mock.date_range), 'Timestamp': MockTimestamp, 'Timedelta': pd.Timedelta})()# pragma: no cover

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
