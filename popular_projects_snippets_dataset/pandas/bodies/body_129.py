# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
df = DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=["a", "a", "c"])

result = df.apply(lambda s: s[0], axis=1)
expected = Series([1, 4, 7], ["a", "a", "c"])
tm.assert_series_equal(result, expected)

result = df.T.apply(lambda s: s[0], axis=0)
tm.assert_series_equal(result, expected)
