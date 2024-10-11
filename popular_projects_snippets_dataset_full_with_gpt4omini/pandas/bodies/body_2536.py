# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
rng = period_range("1/1/2000", periods=5, name="index")
df = DataFrame(np.random.randn(5, 3), index=rng)

df["Index"] = rng
rs = Index(df["Index"])
tm.assert_index_equal(rs, rng, check_names=False)
assert rs.name == "Index"
assert rng.name == "index"

rs = df.reset_index().set_index("index")
assert isinstance(rs.index, PeriodIndex)
tm.assert_index_equal(rs.index, rng)
