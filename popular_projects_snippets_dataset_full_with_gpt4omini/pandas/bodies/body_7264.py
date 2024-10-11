# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_join.py
other = Index(
    2**63 + np.array([1, 5, 7, 10, 20], dtype="uint64"), dtype=object
)

outer = index_large.join(other, how="outer")
outer2 = other.join(index_large, how="outer")
expected = Index(
    2**63 + np.array([0, 1, 5, 7, 10, 15, 20, 25], dtype="uint64")
)
tm.assert_index_equal(outer, outer2)
tm.assert_index_equal(outer, expected)

inner = index_large.join(other, how="inner")
inner2 = other.join(index_large, how="inner")
expected = Index(2**63 + np.array([10, 20], dtype="uint64"))
tm.assert_index_equal(inner, inner2)
tm.assert_index_equal(inner, expected)

left = index_large.join(other, how="left")
tm.assert_index_equal(left, index_large.astype(object))

left2 = other.join(index_large, how="left")
tm.assert_index_equal(left2, other)

right = index_large.join(other, how="right")
tm.assert_index_equal(right, other)

right2 = other.join(index_large, how="right")
tm.assert_index_equal(right2, index_large.astype(object))
