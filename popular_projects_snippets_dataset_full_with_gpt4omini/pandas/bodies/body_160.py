# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
result = float_frame.apply(lambda x: x.name)
expected = Series(float_frame.columns, index=float_frame.columns)
tm.assert_series_equal(result, expected)
