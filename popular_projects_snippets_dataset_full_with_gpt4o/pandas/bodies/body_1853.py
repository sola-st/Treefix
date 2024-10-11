# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resample_api.py
grouped = test_series.to_frame(name="foo").resample("20min", group_keys=False)
result = grouped["foo"].apply(lambda x: x)
tm.assert_series_equal(result, test_series.rename("foo"))
