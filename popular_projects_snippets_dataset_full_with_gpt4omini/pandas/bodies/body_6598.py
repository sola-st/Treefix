# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_setops.py
# GH#12034 Cases where we operate against another RangeIndex and may
#  get back another RangeIndex
left = RangeIndex.from_range(range(1, 10), name="foo")

result = left.symmetric_difference(left)
expected = RangeIndex.from_range(range(0), name="foo")
tm.assert_index_equal(result, expected)

result = left.symmetric_difference(expected.rename("bar"))
tm.assert_index_equal(result, left.rename(None))

result = left[:-2].symmetric_difference(left[2:])
expected = Index([1, 2, 8, 9], name="foo")
tm.assert_index_equal(result, expected, exact=True)

right = RangeIndex.from_range(range(10, 15))

result = left.symmetric_difference(right)
expected = RangeIndex.from_range(range(1, 15))
tm.assert_index_equal(result, expected)

result = left.symmetric_difference(right[1:])
expected = Index([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14])
tm.assert_index_equal(result, expected, exact=True)
