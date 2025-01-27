# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
result = float_frame.apply(lambda x: x.name, axis=1)
expected = Series(float_frame.index, index=float_frame.index)
tm.assert_series_equal(result, expected)
