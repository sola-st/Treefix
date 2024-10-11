# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
Series(np.array([1100, 20], dtype="timedelta64[ns]")).to_string()

s = Series(date_range("2012-1-1", periods=3, freq="D"))

# GH2146

# adding NaTs
y = s - s.shift(1)
result = y.to_string()
assert "1 days" in result
assert "00:00:00" not in result
assert "NaT" in result

# with frac seconds
o = Series([datetime(2012, 1, 1, microsecond=150)] * 3)
y = s - o
result = y.to_string()
assert "-1 days +23:59:59.999850" in result

# rounding?
o = Series([datetime(2012, 1, 1, 1)] * 3)
y = s - o
result = y.to_string()
assert "-1 days +23:00:00" in result
assert "1 days 23:00:00" in result

o = Series([datetime(2012, 1, 1, 1, 1)] * 3)
y = s - o
result = y.to_string()
assert "-1 days +22:59:00" in result
assert "1 days 22:59:00" in result

o = Series([datetime(2012, 1, 1, 1, 1, microsecond=150)] * 3)
y = s - o
result = y.to_string()
assert "-1 days +22:58:59.999850" in result
assert "0 days 22:58:59.999850" in result

# neg time
td = timedelta(minutes=5, seconds=3)
s2 = Series(date_range("2012-1-1", periods=3, freq="D")) + td
y = s - s2
result = y.to_string()
assert "-1 days +23:54:57" in result

td = timedelta(microseconds=550)
s2 = Series(date_range("2012-1-1", periods=3, freq="D")) + td
y = s - td
result = y.to_string()
assert "2012-01-01 23:59:59.999450" in result

# no boxing of the actual elements
td = Series(pd.timedelta_range("1 days", periods=3))
result = td.to_string()
assert result == "0   1 days\n1   2 days\n2   3 days"
