# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_comparison.py
# GH#44382

mask = np.zeros(3, dtype=bool)
data = np.array([1.0, np.nan, 3.0], dtype=np.float64)

left = FloatingArray(data, mask)
assert left.equals(left)
tm.assert_extension_array_equal(left, left)

assert left.equals(left.copy())
assert left.equals(FloatingArray(data.copy(), mask.copy()))

mask2 = np.array([False, True, False], dtype=bool)
data2 = np.array([1.0, 2.0, 3.0], dtype=np.float64)
right = FloatingArray(data2, mask2)
assert right.equals(right)
tm.assert_extension_array_equal(right, right)

assert not left.equals(right)

# with mask[1] = True, the only difference is data[1], which should
#  not matter for equals
mask[1] = True
assert left.equals(right)
