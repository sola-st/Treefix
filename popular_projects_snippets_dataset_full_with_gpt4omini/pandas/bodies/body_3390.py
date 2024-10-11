# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# https://github.com/pandas-dev/pandas/issues/32988
df = DataFrame(np.eye(2), dtype=dtype)
result = df.replace(to_replace=[None, -np.inf, np.inf], value=value)
tm.assert_frame_equal(result, df)
