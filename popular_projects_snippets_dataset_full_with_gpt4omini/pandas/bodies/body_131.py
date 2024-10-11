# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
result = float_frame.apply(np.mean, axis=1, result_type="broadcast")
m = float_frame.mean(axis=1)
expected = DataFrame({c: m for c in float_frame.columns})
tm.assert_frame_equal(result, expected)
