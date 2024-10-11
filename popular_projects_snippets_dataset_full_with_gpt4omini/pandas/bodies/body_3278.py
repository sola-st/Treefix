# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
# issue mentioned further down in the following issue's thread
# https://github.com/pandas-dev/pandas/issues/33113
df = DataFrame()
result = df.astype({})
tm.assert_frame_equal(result, df)
assert result is not df
