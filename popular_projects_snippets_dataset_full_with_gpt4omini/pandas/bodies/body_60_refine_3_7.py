import pandas as pd # pragma: no cover
from pandas import Series # pragma: no cover

import pandas as pd # pragma: no cover
from pandas import Series # pragma: no cover

pd = type('Mock', (object,), {})() # pragma: no cover
pd.date_range = staticmethod(lambda start, periods: [pd.Timestamp(start) + pd.Timedelta(days=i) for i in range(periods)]) # pragma: no cover
pd.Timestamp = type('Timestamp', (object,), {'__init__': lambda self, date_str: setattr(self, 'date', date_str), '__str__': lambda self: self.date}) # pragma: no cover
pd.Timedelta = type('Timedelta', (object,), {'__init__': lambda self, days: setattr(self, 'days', days), '__add__': lambda self, other: pd.Timestamp(str(int(self.days) + int(other.days)))}) # pragma: no cover

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
