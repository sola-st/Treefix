import pandas as pd # pragma: no cover
from pandas import Series # pragma: no cover

import pandas as pd # pragma: no cover
from pandas import Series # pragma: no cover

pd.Timestamp = type('Mock', (object,), {'__init__': lambda self, d: setattr(self, 'value', d), '__add__': lambda self, other: pd.Timestamp(str(self.value + other)), '__sub__': lambda self, other: pd.Timestamp(str(self.value - other)), '__repr__': lambda self: f'Timestamp({self.value})'}) # pragma: no cover
pd.Timedelta = type('Mock', (object,), {'__init__': lambda self, d: setattr(self, 'days', d.days if hasattr(d, 'days') else 0), '__add__': lambda self, other: pd.Timedelta(days=self.days + other.days), '__repr__': lambda self: f'Timedelta({self.days})'}) # pragma: no cover
pd.date_range = staticmethod(lambda start, periods: [pd.Timestamp(start) + pd.Timedelta(days=i) for i in range(periods)]) # pragma: no cover
Series = pd.Series # pragma: no cover

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
