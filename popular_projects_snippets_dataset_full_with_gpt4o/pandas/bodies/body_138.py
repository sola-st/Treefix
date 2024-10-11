# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
result = float_frame.apply(np.mean, axis=axis, raw=True)
expected = float_frame.apply(lambda x: x.values.mean(), axis=axis)
tm.assert_series_equal(result, expected)
