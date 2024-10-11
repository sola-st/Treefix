# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resampler_grouper.py
# GH: 36951
df = DataFrame(
    {"col": range(10), "col1": range(10, 20)},
    index=date_range("2012-01-01", periods=10, freq="20min"),
)

# access "col" via getattr -> make sure we handle AttributeError
result = df.resample("H").apply(lambda group: group.col.sum())
expected = Series(
    [3, 12, 21, 9], index=date_range("2012-01-01", periods=4, freq="H")
)
tm.assert_series_equal(result, expected)

# access "col" via _getitem__ -> make sure we handle KeyErrpr
result = df.resample("H").apply(lambda group: group["col"].sum())
tm.assert_series_equal(result, expected)
