# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_constructors.py

result = RangeIndex.from_range(range(1, 5, 2))
expected = RangeIndex(1, 5, 2)
tm.assert_index_equal(result, expected, exact=True)

result = RangeIndex.from_range(range(5, 6))
expected = RangeIndex(5, 6, 1)
tm.assert_index_equal(result, expected, exact=True)

# an invalid range
result = RangeIndex.from_range(range(5, 1))
expected = RangeIndex(0, 0, 1)
tm.assert_index_equal(result, expected, exact=True)

result = RangeIndex.from_range(range(5))
expected = RangeIndex(0, 5, 1)
tm.assert_index_equal(result, expected, exact=True)

result = Index(range(1, 5, 2))
expected = RangeIndex(1, 5, 2)
tm.assert_index_equal(result, expected, exact=True)

msg = (
    r"(RangeIndex.)?from_range\(\) got an unexpected keyword argument( 'copy')?"
)
with pytest.raises(TypeError, match=msg):
    RangeIndex.from_range(range(10), copy=True)
