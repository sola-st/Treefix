import pandas as pd # pragma: no cover
from pandas import Series # pragma: no cover

import pandas as pd # pragma: no cover
from pandas import Series # pragma: no cover

class MockDateTime:# pragma: no cover
    def __init__(self, date_time):# pragma: no cover
        self.date_time = date_time# pragma: no cover
    @property# pragma: no cover
    def hour(self):# pragma: no cover
        return self.date_time.hour# pragma: no cover
    @property# pragma: no cover
    def day(self):# pragma: no cover
        return self.date_time.day# pragma: no cover
    @property# pragma: no cover
    def month(self):# pragma: no cover
        return self.date_time.month# pragma: no cover
    def __call__(self, *args, **kwargs):# pragma: no cover
        return self# pragma: no cover
# pragma: no cover
pd.Timestamp = MockDateTime # pragma: no cover

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
