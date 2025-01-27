# Extracted from ./data/repos/pandas/pandas/tests/window/test_apply.py
# GH 45912
df = DataFrame([1, 2])
result = df.rolling(window=1, axis=1).apply(np.sum, raw=raw)
expected = DataFrame([1.0, 2.0])
tm.assert_frame_equal(result, expected)
