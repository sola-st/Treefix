# Extracted from ./data/repos/pandas/pandas/tests/resample/test_time_grouper.py
result = test_series.resample("A", closed="right").prod()

expected = test_series.groupby(lambda x: x.year).agg(np.prod)
expected.index = result.index

tm.assert_series_equal(result, expected)
