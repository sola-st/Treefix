# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_asof.py
# Explicitly cast to float to avoid implicit cast when setting np.nan
df = date_range_frame.astype({"A": "float"})
N = 50
df.loc[df.index[15:30], "A"] = np.nan
dates = date_range("1/1/1990", periods=N * 3, freq="25s")

result = df.asof(dates)
assert result.notna().all(1).all()
lb = df.index[14]
ub = df.index[30]

dates = list(dates)

result = df.asof(dates)
assert result.notna().all(1).all()

mask = (result.index >= lb) & (result.index < ub)
rs = result[mask]
assert (rs == 14).all(1).all()
