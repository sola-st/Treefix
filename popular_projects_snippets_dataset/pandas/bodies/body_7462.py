# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_setops.py
piece1 = idx[:5][::-1]
piece2 = idx[3:]

the_int = piece1.intersection(piece2, sort=sort)

if sort is None:
    tm.assert_index_equal(the_int, idx[3:5])
assert tm.equalContents(the_int, idx[3:5])

# corner case, pass self
the_int = idx.intersection(idx, sort=sort)
tm.assert_index_equal(the_int, idx)

# empty intersection: disjoint
empty = idx[:2].intersection(idx[2:], sort=sort)
expected = idx[:0]
assert empty.equals(expected)

tuples = idx.values
result = idx.intersection(tuples)
assert result.equals(idx)
