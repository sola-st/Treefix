# Extracted from ./data/repos/pandas/pandas/tests/extension/base/casting.py
# https://github.com/pandas-dev/pandas/issues/33113
df = pd.DataFrame()
result = df.astype(dtype)
self.assert_frame_equal(result, df)
