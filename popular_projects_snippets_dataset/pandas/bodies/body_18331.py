# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# series ops
v1 = pd.date_range("2012-1-1", periods=3, freq="D")
v2 = pd.date_range("2012-1-2", periods=3, freq="D")
rs = Series(v2) - Series(v1)
xp = Series(1e9 * 3600 * 24, rs.index).astype("int64").astype("timedelta64[ns]")
tm.assert_series_equal(rs, xp)
assert rs.dtype == "timedelta64[ns]"

df = DataFrame({"A": v1})
td = Series([timedelta(days=i) for i in range(3)])
assert td.dtype == "timedelta64[ns]"

# series on the rhs
result = df["A"] - df["A"].shift()
assert result.dtype == "timedelta64[ns]"

result = df["A"] + td
assert result.dtype == "M8[ns]"

# scalar Timestamp on rhs
maxa = df["A"].max()
assert isinstance(maxa, Timestamp)

resultb = df["A"] - df["A"].max()
assert resultb.dtype == "timedelta64[ns]"

# timestamp on lhs
result = resultb + df["A"]
values = [Timestamp("20111230"), Timestamp("20120101"), Timestamp("20120103")]
expected = Series(values, name="A")
tm.assert_series_equal(result, expected)

# datetimes on rhs
result = df["A"] - datetime(2001, 1, 1)
expected = Series([timedelta(days=4017 + i) for i in range(3)], name="A")
tm.assert_series_equal(result, expected)
assert result.dtype == "m8[ns]"

d = datetime(2001, 1, 1, 3, 4)
resulta = df["A"] - d
assert resulta.dtype == "m8[ns]"

# roundtrip
resultb = resulta + d
tm.assert_series_equal(df["A"], resultb)

# timedeltas on rhs
td = timedelta(days=1)
resulta = df["A"] + td
resultb = resulta - td
tm.assert_series_equal(resultb, df["A"])
assert resultb.dtype == "M8[ns]"

# roundtrip
td = timedelta(minutes=5, seconds=3)
resulta = df["A"] + td
resultb = resulta - td
tm.assert_series_equal(df["A"], resultb)
assert resultb.dtype == "M8[ns]"

# inplace
value = rs[2] + np.timedelta64(timedelta(minutes=5, seconds=1))
rs[2] += np.timedelta64(timedelta(minutes=5, seconds=1))
assert rs[2] == value
