# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_asof.py

# array or list or dates
N = 50
rng = date_range("1/1/1990", periods=N, freq="53s")
ts = Series(np.random.randn(N), index=rng)
ts.iloc[15:30] = np.nan
dates = date_range("1/1/1990", periods=N * 3, freq="25s")

result = ts.asof(dates)
assert notna(result).all()
lb = ts.index[14]
ub = ts.index[30]

result = ts.asof(list(dates))
assert notna(result).all()
lb = ts.index[14]
ub = ts.index[30]

mask = (result.index >= lb) & (result.index < ub)
rs = result[mask]
assert (rs == ts[lb]).all()

val = result[result.index[result.index >= ub][0]]
assert ts[ub] == val
