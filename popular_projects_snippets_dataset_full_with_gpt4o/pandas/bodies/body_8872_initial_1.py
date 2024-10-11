import numpy as np # pragma: no cover
from pandas.arrays import DatetimeArray # pragma: no cover
import pandas as pd # pragma: no cover

tz = "US/Eastern" # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
# GH#49684
from l3.Runtime import _l_
utc_vals = np.array(
    [1320552000, 1320555600, 1320559200, 1320562800], dtype=np.int64
)
_l_(21518)
utc_vals *= 1_000_000_000
_l_(21519)

dta = DatetimeArray(utc_vals).tz_localize("UTC").tz_convert(tz)
_l_(21520)

left = dta[2]
_l_(21521)
right = list(dta)[2]
_l_(21522)
assert str(left) == str(right)
_l_(21523)
# previously there was a bug where with non-pytz right would be
#  Timestamp('2011-11-06 01:00:00-0400', tz='US/Eastern')
# while left would be
#  Timestamp('2011-11-06 01:00:00-0500', tz='US/Eastern')
# The .value's would match (so they would compare as equal),
#  but the folds would not
assert left.utcoffset() == right.utcoffset()
_l_(21524)

# The same bug in ints_to_pydatetime affected .astype, so we test
#  that here.
right2 = dta.astype(object)[2]
_l_(21525)
assert str(left) == str(right2)
_l_(21526)
assert left.utcoffset() == right2.utcoffset()
_l_(21527)
