# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reset_index.py
# GH 6878
result = float_frame.reset_index(names="new_name")
expected = Series(float_frame.index.values, name="new_name")
tm.assert_series_equal(result["new_name"], expected)

result = float_frame.reset_index(names=123)
expected = Series(float_frame.index.values, name=123)
tm.assert_series_equal(result[123], expected)
