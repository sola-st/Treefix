# Extracted from ./data/repos/pandas/pandas/tests/generic/test_generic.py
# don't fail with 0 length dimensions GH11229 & GH8999
empty_series = Series([], name="five", dtype=np.float64)
empty_frame = DataFrame([empty_series])
tm.assert_series_equal(empty_series, empty_series.squeeze())
tm.assert_series_equal(empty_series, empty_frame.squeeze())
