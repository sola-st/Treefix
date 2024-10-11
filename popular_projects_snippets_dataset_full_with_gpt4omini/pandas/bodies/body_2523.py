# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
rng = date_range("1/1/2000 00:00:00", "1/1/2000 1:59:50", freq="10s")
df = DataFrame(index=np.arange(len(rng)))

df["A"] = rng
assert df["A"].dtype == np.dtype("M8[ns]")
