# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_interpolate.py
# https://github.com/pandas-dev/pandas/issues/35598
df = DataFrame()
result = df.interpolate()
assert result is not df
expected = df
tm.assert_frame_equal(result, expected)
