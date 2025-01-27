# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_setops.py
# name retention on empty intersections
index = RangeIndex(start=0, stop=20, step=2, name=names[0])

# empty other
result = index.intersection(index[:0].rename(names[1]), sort=sort)
tm.assert_index_equal(result, index[:0].rename(names[2]), exact=True)

# empty self
result = index[:0].intersection(index.rename(names[1]), sort=sort)
tm.assert_index_equal(result, index[:0].rename(names[2]), exact=True)
