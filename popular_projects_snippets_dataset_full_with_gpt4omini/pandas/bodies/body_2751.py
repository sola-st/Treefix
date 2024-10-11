# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_truncate.py
rng = date_range("2011-01-01", "2012-01-01", freq="W")
ts = DataFrame(
    {"A": np.random.randn(len(rng)), "B": np.random.randn(len(rng))}, index=rng
)

decreasing = ts.sort_values("A", ascending=False)

msg = "truncate requires a sorted index"
with pytest.raises(ValueError, match=msg):
    decreasing.truncate(before="2011-11", after="2011-12")
