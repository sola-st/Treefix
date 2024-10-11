import numpy as np # pragma: no cover
import pytz # pragma: no cover

tz = pytz.timezone('US/Eastern') # pragma: no cover
np = type('Mock', (object,), {'array': np.array, 'int64': np.int64})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
# GH#49684
from l3.Runtime import _l_
utc_vals = np.array(
    [1320552000, 1320555600, 1320559200, 1320562800], dtype=np.int64
)
_l_(10372)
utc_vals *= 1_000_000_000
_l_(10373)

dta = DatetimeArray(utc_vals).tz_localize("UTC").tz_convert(tz)
_l_(10374)

left = dta[2]
_l_(10375)
right = list(dta)[2]
_l_(10376)
assert str(left) == str(right)
_l_(10377)
# previously there was a bug where with non-pytz right would be
#  Timestamp('2011-11-06 01:00:00-0400', tz='US/Eastern')
# while left would be
#  Timestamp('2011-11-06 01:00:00-0500', tz='US/Eastern')
# The .value's would match (so they would compare as equal),
#  but the folds would not
assert left.utcoffset() == right.utcoffset()
_l_(10378)

# The same bug in ints_to_pydatetime affected .astype, so we test
#  that here.
right2 = dta.astype(object)[2]
_l_(10379)
assert str(left) == str(right2)
_l_(10380)
assert left.utcoffset() == right2.utcoffset()
_l_(10381)
