# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# Make sure we don't accidentally treat timedelta64(NaT) as datetime64
#  when calling dispatch_to_series in DataFrame arithmetic
ser = Series(["NaT", "NaT"], dtype="timedelta64[ns]")
df = DataFrame([[1, 2], [3, 4]])

result = df * ser
expected = DataFrame({0: ser, 1: ser})
tm.assert_frame_equal(result, expected)
