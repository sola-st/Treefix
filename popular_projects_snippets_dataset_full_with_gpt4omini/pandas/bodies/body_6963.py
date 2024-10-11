# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
# GH#20040
# Test that the intersection of an index with an
# empty index produces the same index as the difference
# of an index with itself.  Test for all types
if not index.is_unique:
    exit()
inter = index.intersection(index[:0])
diff = index.difference(index, sort=sort)
tm.assert_index_equal(inter, diff, exact=True)
