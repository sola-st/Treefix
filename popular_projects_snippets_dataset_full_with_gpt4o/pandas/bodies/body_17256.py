# Extracted from ./data/repos/pandas/pandas/tests/generic/test_series.py
# resample
ts = Series(
    np.random.rand(1000),
    index=date_range("20130101", periods=1000, freq="s"),
    name="foo",
)
result = ts.resample("1T").mean()
tm.assert_metadata_equivalent(ts, result)

result = ts.resample("1T").min()
tm.assert_metadata_equivalent(ts, result)

result = ts.resample("1T").apply(lambda x: x.sum())
tm.assert_metadata_equivalent(ts, result)
