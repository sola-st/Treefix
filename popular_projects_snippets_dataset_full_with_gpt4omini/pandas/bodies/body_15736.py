# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_asof.py

N = 30
rng = date_range("1/1/1990", periods=N, freq="53s")
# Explicit cast to float avoid implicit cast when setting nan
ts = Series(np.arange(N), index=rng, dtype="float")
ts.iloc[5:10] = np.NaN
ts.iloc[15:20] = np.NaN

val1 = ts.asof(ts.index[7])
val2 = ts.asof(ts.index[19])

assert val1 == ts[4]
assert val2 == ts[14]

# accepts strings
val1 = ts.asof(str(ts.index[7]))
assert val1 == ts[4]

# in there
result = ts.asof(ts.index[3])
assert result == ts[3]

# no as of value
d = ts.index[0] - offsets.BDay()
assert np.isnan(ts.asof(d))
