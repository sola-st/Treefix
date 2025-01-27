# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_setops.py

first = idx
result = first.difference(idx[-3:], sort=sort)
vals = idx[:-3].values

if sort is None:
    vals = sorted(vals)

expected = MultiIndex.from_tuples(vals, sortorder=0, names=idx.names)

assert isinstance(result, MultiIndex)
assert result.equals(expected)
assert result.names == idx.names
tm.assert_index_equal(result, expected)

# empty difference: reflexive
result = idx.difference(idx, sort=sort)
expected = idx[:0]
assert result.equals(expected)
assert result.names == idx.names

# empty difference: superset
result = idx[-3:].difference(idx, sort=sort)
expected = idx[:0]
assert result.equals(expected)
assert result.names == idx.names

# empty difference: degenerate
result = idx[:0].difference(idx, sort=sort)
expected = idx[:0]
assert result.equals(expected)
assert result.names == idx.names

# names not the same
chunklet = idx[-3:]
chunklet.names = ["foo", "baz"]
result = first.difference(chunklet, sort=sort)
assert result.names == (None, None)

# empty, but non-equal
result = idx.difference(idx.sortlevel(1)[0], sort=sort)
assert len(result) == 0

# raise Exception called with non-MultiIndex
result = first.difference(first.values, sort=sort)
assert result.equals(first[:0])

# name from empty array
result = first.difference([], sort=sort)
assert first.equals(result)
assert first.names == result.names

# name from non-empty array
result = first.difference([("foo", "one")], sort=sort)
expected = MultiIndex.from_tuples(
    [("bar", "one"), ("baz", "two"), ("foo", "two"), ("qux", "one"), ("qux", "two")]
)
expected.names = first.names
assert first.names == result.names

msg = "other must be a MultiIndex or a list of tuples"
with pytest.raises(TypeError, match=msg):
    first.difference([1, 2, 3, 4, 5], sort=sort)
