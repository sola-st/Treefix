# Extracted from ./data/repos/pandas/pandas/tests/window/test_win_type.py
df = DataFrame(
    {"a": [1, 1, 0, 0, 0, 1], "b": [1, 0, 0, 1, 0, 0], "c": [1, 0, 0, 1, 0, 1]}
)

result = df.rolling(window=3, axis=1, win_type="boxcar", center=True).sum()

expected = DataFrame(
    {"a": [np.nan] * 6, "b": [3.0, 1.0, 0.0, 2.0, 0.0, 2.0], "c": [np.nan] * 6}
)

tm.assert_frame_equal(result, expected, check_dtype=True)
