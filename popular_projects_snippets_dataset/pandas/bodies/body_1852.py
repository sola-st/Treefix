# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resample_api.py
# both resample and groupby should work w/o aggregation
t = func(test_series)
result = t.apply(lambda x: x)
tm.assert_series_equal(result, test_series)
