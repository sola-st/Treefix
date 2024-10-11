# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_setops.py
everything = tm.makeDateIndex(10)
first = everything[:5]
second = everything[5:]
union = first.union(second, sort=sort)
tm.assert_index_equal(union, everything)
