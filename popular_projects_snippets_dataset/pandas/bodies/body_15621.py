# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_equals.py
# matching but not identical NAs
left = Series([np.datetime64("NaT")], dtype=object)
right = Series([np.datetime64("NaT")], dtype=object)
assert left.equals(right)
assert Index(left).equals(Index(right))
assert left.array.equals(right.array)

left = Series([np.timedelta64("NaT")], dtype=object)
right = Series([np.timedelta64("NaT")], dtype=object)
assert left.equals(right)
assert Index(left).equals(Index(right))
assert left.array.equals(right.array)

left = Series([np.float64("NaN")], dtype=object)
right = Series([np.float64("NaN")], dtype=object)
assert left.equals(right)
assert Index(left, dtype=left.dtype).equals(Index(right, dtype=right.dtype))
assert left.array.equals(right.array)
