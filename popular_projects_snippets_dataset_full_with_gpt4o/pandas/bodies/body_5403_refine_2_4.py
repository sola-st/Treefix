from datetime import datetime # pragma: no cover
import pandas as pd # pragma: no cover
import pytz # pragma: no cover

Timestamp = pd.Timestamp # pragma: no cover
tz = pytz.timezone('US/Eastern') # pragma: no cover
unit = 'us' # pragma: no cover
fold = 1 # pragma: no cover

from datetime import datetime # pragma: no cover
import pandas as pd # pragma: no cover
import pytz # pragma: no cover
import numpy as np # pragma: no cover

Timestamp = pd.Timestamp # pragma: no cover
tz = pytz.timezone('US/Eastern') # pragma: no cover
unit = 'us' # pragma: no cover
fold = 1 # pragma: no cover
NpyDatetimeUnit = type('NpyDatetimeUnit', (object,), {'NPY_FR_us': type('Mock', (object,), {'value': np.int64(10**3)})()}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_unary_ops.py
# GH 25017
from l3.Runtime import _l_
d = datetime(2019, 10, 27, 2, 30)
_l_(17568)
ts = Timestamp(d, tz=tz).as_unit(unit)
_l_(17569)
result = ts.replace(hour=1, fold=fold)
_l_(17570)
expected = Timestamp(datetime(2019, 10, 27, 1, 30)).tz_localize(
    tz, ambiguous=not fold
)
_l_(17571)
assert result == expected
_l_(17572)
assert result._creso == getattr(NpyDatetimeUnit, f"NPY_FR_{unit}").value
_l_(17573)
