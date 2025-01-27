# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py

# 8260
# support datetime64 with tz

from l3.Runtime import _l_
dr = date_range("20130101", periods=3, tz="US/Eastern")
_l_(20536)
s = Series(dr)
_l_(20537)
assert s.dtype.name == "datetime64[ns, US/Eastern]"
_l_(20538)
assert s.dtype == "datetime64[ns, US/Eastern]"
_l_(20539)
assert is_datetime64tz_dtype(s.dtype)
_l_(20540)
assert "datetime64[ns, US/Eastern]" in str(s)
_l_(20541)

# export
result = s.values
_l_(20542)
assert isinstance(result, np.ndarray)
_l_(20543)
assert result.dtype == "datetime64[ns]"
_l_(20544)

exp = DatetimeIndex(result)
_l_(20545)
exp = exp.tz_localize("UTC").tz_convert(tz=s.dt.tz)
_l_(20546)
tm.assert_index_equal(dr, exp)
_l_(20547)

# indexing
result = s.iloc[0]
_l_(20548)
assert result == Timestamp("2013-01-01 00:00:00-0500", tz="US/Eastern")
_l_(20549)
result = s[0]
_l_(20550)
assert result == Timestamp("2013-01-01 00:00:00-0500", tz="US/Eastern")
_l_(20551)

result = s[Series([True, True, False], index=s.index)]
_l_(20552)
tm.assert_series_equal(result, s[0:2])
_l_(20553)

result = s.iloc[0:1]
_l_(20554)
tm.assert_series_equal(result, Series(dr[0:1]))
_l_(20555)

# concat
result = pd.concat([s.iloc[0:1], s.iloc[1:]])
_l_(20556)
tm.assert_series_equal(result, s)
_l_(20557)

# short str
assert "datetime64[ns, US/Eastern]" in str(s)
_l_(20558)

# formatting with NaT
result = s.shift()
_l_(20559)
assert "datetime64[ns, US/Eastern]" in str(result)
_l_(20560)
assert "NaT" in str(result)
_l_(20561)

# long str
t = Series(date_range("20130101", periods=1000, tz="US/Eastern"))
_l_(20562)
assert "datetime64[ns, US/Eastern]" in str(t)
_l_(20563)

result = DatetimeIndex(s, freq="infer")
_l_(20564)
tm.assert_index_equal(result, dr)
_l_(20565)
