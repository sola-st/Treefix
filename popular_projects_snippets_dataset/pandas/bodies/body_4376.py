# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# https://github.com/pandas-dev/pandas/issues/21083
df = DataFrame({"A": ["x", None]}, dtype=string_dtype)
result = df.isna()
expected = DataFrame({"A": [False, True]})
tm.assert_frame_equal(result, expected)
assert df.iloc[1, 0] is None

df = DataFrame({"A": ["x", np.nan]}, dtype=string_dtype)
assert np.isnan(df.iloc[1, 0])
