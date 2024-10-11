import pandas as pd # pragma: no cover
from pandas import Series # pragma: no cover

import pandas as pd # pragma: no cover
from pandas import Series # pragma: no cover

class MockTimestamp:  # Simulating Timestamp object# pragma: no cover
    def __init__(self, value):# pragma: no cover
        self.value = pd.to_datetime(value)# pragma: no cover
        self.hour = self.value.hour# pragma: no cover
        self.day = self.value.day# pragma: no cover
        self.month = self.value.month# pragma: no cover
# pragma: no cover
class MockTimedelta:  # Simulating Timedelta object# pragma: no cover
    def __init__(self, days):# pragma: no cover
        self.days = days# pragma: no cover
# pragma: no cover
pd = type('Mock', (object,), {# pragma: no cover
    'Timestamp': MockTimestamp,# pragma: no cover
    'Timedelta': MockTimedelta,# pragma: no cover
    'date_range': staticmethod(lambda start, periods: [MockTimestamp(start) + MockTimedelta(i) for i in range(periods)])# pragma: no cover
})() # pragma: no cover
Series = pd.__class__  # Assigning Series to the Mock class # pragma: no cover

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
