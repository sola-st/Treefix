# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_constructors.py

# pass thru w and w/o copy
index = RangeIndex(1, 5, 2)
result = RangeIndex(index, copy=False)
assert result.identical(index)

result = RangeIndex(index, copy=True)
tm.assert_index_equal(result, index, exact=True)

result = RangeIndex(index)
tm.assert_index_equal(result, index, exact=True)

with pytest.raises(
    ValueError,
    match="Incorrect `dtype` passed: expected signed integer, received float64",
):
    RangeIndex(index, dtype="float64")
