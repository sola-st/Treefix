from pandas import date_range, Timestamp, Timedelta # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_misc.py
# GH#37295 should hold for any DTI with freq=None or Tick freq
from l3.Runtime import _l_
tz = "Canada/Eastern"
_l_(21014)
dti = date_range(
    start=Timestamp("2019-03-26 00:00:00-0400", tz=tz),
    end=Timestamp("2020-10-17 00:00:00-0400", tz=tz),
    freq="D",
)
_l_(21015)
result = dti + Timedelta(days=1)
_l_(21016)
assert result.freq == dti.freq
_l_(21017)
