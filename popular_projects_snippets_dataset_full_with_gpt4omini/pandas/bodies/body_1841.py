# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resample_api.py
# GH17905

# series
r = test_series.resample("H")
expected = r.max() - r.mean()
result = r.pipe(lambda x: x.max() - x.mean())
tm.assert_series_equal(result, expected)

# dataframe
r = test_frame.resample("H")
expected = r.max() - r.mean()
result = r.pipe(lambda x: x.max() - x.mean())
tm.assert_frame_equal(result, expected)
