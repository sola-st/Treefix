import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover
from pandas import date_range, Series, DatetimeIndex, Timestamp # pragma: no cover
from pandas.api.types import is_datetime64tz_dtype # pragma: no cover
import pandas.testing as tm # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py

# 8260
# support datetime64 with tz

from l3.Runtime import _l_
dr = date_range("20130101", periods=3, tz="US/Eastern")
_l_(9023)
s = Series(dr)
_l_(9024)
assert s.dtype.name == "datetime64[ns, US/Eastern]"
_l_(9025)
assert s.dtype == "datetime64[ns, US/Eastern]"
_l_(9026)
assert is_datetime64tz_dtype(s.dtype)
_l_(9027)
assert "datetime64[ns, US/Eastern]" in str(s)
_l_(9028)

# export
result = s.values
_l_(9029)
assert isinstance(result, np.ndarray)
_l_(9030)
assert result.dtype == "datetime64[ns]"
_l_(9031)

exp = DatetimeIndex(result)
_l_(9032)
exp = exp.tz_localize("UTC").tz_convert(tz=s.dt.tz)
_l_(9033)
tm.assert_index_equal(dr, exp)
_l_(9034)

# indexing
result = s.iloc[0]
_l_(9035)
assert result == Timestamp("2013-01-01 00:00:00-0500", tz="US/Eastern")
_l_(9036)
result = s[0]
_l_(9037)
assert result == Timestamp("2013-01-01 00:00:00-0500", tz="US/Eastern")
_l_(9038)

result = s[Series([True, True, False], index=s.index)]
_l_(9039)
tm.assert_series_equal(result, s[0:2])
_l_(9040)

result = s.iloc[0:1]
_l_(9041)
tm.assert_series_equal(result, Series(dr[0:1]))
_l_(9042)

# concat
result = pd.concat([s.iloc[0:1], s.iloc[1:]])
_l_(9043)
tm.assert_series_equal(result, s)
_l_(9044)

# short str
assert "datetime64[ns, US/Eastern]" in str(s)
_l_(9045)

# formatting with NaT
result = s.shift()
_l_(9046)
assert "datetime64[ns, US/Eastern]" in str(result)
_l_(9047)
assert "NaT" in str(result)
_l_(9048)

# long str
t = Series(date_range("20130101", periods=1000, tz="US/Eastern"))
_l_(9049)
assert "datetime64[ns, US/Eastern]" in str(t)
_l_(9050)

result = DatetimeIndex(s, freq="infer")
_l_(9051)
tm.assert_index_equal(result, dr)
_l_(9052)
