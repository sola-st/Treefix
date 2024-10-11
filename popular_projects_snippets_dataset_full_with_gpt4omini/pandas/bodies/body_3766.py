# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_align.py
# GH#
df = DataFrame({0: [1, 2]})
ser = Series([1], name=0)
expected = ser.copy()
result, other = df.align(ser, axis=1)
ser.iloc[0] = 100
tm.assert_series_equal(other, expected)
