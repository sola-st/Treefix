from datetime import datetime # pragma: no cover
import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

tz = 'UTC' # pragma: no cover
unit = 's' # pragma: no cover
fold = False # pragma: no cover
Timestamp = pd.Timestamp # pragma: no cover
NpyDatetimeUnit = type('Mock', (object,), {'NPY_FR_s': type('Mock', (object,), {'value': 1})()}) # pragma: no cover

from datetime import datetime # pragma: no cover
import pandas as pd # pragma: no cover
import pytz # pragma: no cover

tz = pytz.timezone('UTC') # pragma: no cover
unit = 's' # pragma: no cover
fold = False # pragma: no cover
d = datetime(2019, 10, 27, 2, 30) # pragma: no cover
Timestamp = pd.Timestamp # pragma: no cover
class NpyDatetimeUnit: # pragma: no cover
    NPY_FR_s = type('Mock', (object,), {'value': 1})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_unary_ops.py
# GH 25017
from l3.Runtime import _l_
d = datetime(2019, 10, 27, 2, 30)
_l_(5175)
ts = Timestamp(d, tz=tz).as_unit(unit)
_l_(5176)
result = ts.replace(hour=1, fold=fold)
_l_(5177)
expected = Timestamp(datetime(2019, 10, 27, 1, 30)).tz_localize(
    tz, ambiguous=not fold
)
_l_(5178)
assert result == expected
_l_(5179)
assert result._creso == getattr(NpyDatetimeUnit, f"NPY_FR_{unit}").value
_l_(5180)
