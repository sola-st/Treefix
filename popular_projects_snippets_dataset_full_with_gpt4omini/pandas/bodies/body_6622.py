# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py

idx = RangeIndex(5, name="Foo")
expected = idx[1:]
result = idx.delete(0)
tm.assert_index_equal(result, expected, exact=True)
assert result.name == expected.name

expected = idx[:-1]
result = idx.delete(-1)
tm.assert_index_equal(result, expected, exact=True)
assert result.name == expected.name

msg = "index 5 is out of bounds for axis 0 with size 5"
with pytest.raises((IndexError, ValueError), match=msg):
    # either depending on numpy version
    result = idx.delete(len(idx))
