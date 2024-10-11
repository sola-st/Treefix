# Extracted from ./data/repos/pandas/pandas/tests/resample/test_time_grouper.py
test_series[::3] = np.nan

expected = test_series.groupby(lambda x: x.year).count()

grouper = Grouper(freq="A", label="right", closed="right")
result = test_series.groupby(grouper).count()
expected.index = result.index
tm.assert_series_equal(result, expected)

result = test_series.resample("A").count()
expected.index = result.index
tm.assert_series_equal(result, expected)
