# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# scalars
result = float_frame.apply(np.mean, result_type="broadcast")
expected = DataFrame([float_frame.mean()], index=float_frame.index)
tm.assert_frame_equal(result, expected)
