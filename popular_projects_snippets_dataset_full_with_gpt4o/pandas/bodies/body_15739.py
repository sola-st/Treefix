# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_asof.py

s = Series(
    [1, 2, 3],
    index=[Timestamp("20130101"), Timestamp("20130103"), Timestamp("20130102")],
)

# non-monotonic
assert not s.index.is_monotonic_increasing
with pytest.raises(ValueError, match="requires a sorted index"):
    s.asof(s.index[0])

# subset with Series
N = 10
rng = date_range("1/1/1990", periods=N, freq="53s")
s = Series(np.random.randn(N), index=rng)
with pytest.raises(ValueError, match="not valid for Series"):
    s.asof(s.index[0], subset="foo")
