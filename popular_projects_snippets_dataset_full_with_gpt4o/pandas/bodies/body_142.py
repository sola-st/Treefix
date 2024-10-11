# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
d = float_frame.index[0]
result = float_frame.apply(np.mean, axis=1)[d]
expected = np.mean(float_frame.xs(d))
assert result == expected
