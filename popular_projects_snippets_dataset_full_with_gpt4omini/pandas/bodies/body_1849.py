# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resample_api.py
r = test_series.resample("20min")
expected = test_series.groupby(pd.Grouper(freq="20min")).transform("mean")
result = r.transform("mean")
tm.assert_series_equal(result, expected)
