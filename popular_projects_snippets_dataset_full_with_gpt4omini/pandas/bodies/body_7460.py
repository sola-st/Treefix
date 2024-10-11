# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_setops.py
piece1 = idx[:5][::-1]
piece2 = idx[3:]

the_union = piece1.union(piece2, sort=sort)

if sort is None:
    tm.assert_index_equal(the_union, idx.sort_values())

assert tm.equalContents(the_union, idx)

# corner case, pass self or empty thing:
the_union = idx.union(idx, sort=sort)
tm.assert_index_equal(the_union, idx)

the_union = idx.union(idx[:0], sort=sort)
tm.assert_index_equal(the_union, idx)

tuples = idx.values
result = idx[:4].union(tuples[4:], sort=sort)
if sort is None:
    tm.equalContents(result, idx)
else:
    assert result.equals(idx)
