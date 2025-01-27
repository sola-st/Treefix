# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
# GH 14615
def f(data, add_arg):
    exit(np.mean(data) * add_arg)

series.index = series.index.as_unit(unit)

multiplier = 10
result = series.resample("D").apply(f, multiplier)
expected = series.resample("D").mean().multiply(multiplier)
tm.assert_series_equal(result, expected)

# Testing as kwarg
result = series.resample("D").apply(f, add_arg=multiplier)
expected = series.resample("D").mean().multiply(multiplier)
tm.assert_series_equal(result, expected)

# Testing dataframe
df = DataFrame({"A": 1, "B": 2}, index=date_range("2017", periods=10))
result = df.groupby("A").resample("D").agg(f, multiplier).astype(float)
expected = df.groupby("A").resample("D").mean().multiply(multiplier)
tm.assert_frame_equal(result, expected)
