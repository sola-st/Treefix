# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
first = index[:20]
second = index[:10]
intersect = first.intersection(second, sort=sort)
if sort is None:
    tm.assert_index_equal(intersect, second.sort_values())
assert tm.equalContents(intersect, second)

# Corner cases
inter = first.intersection(first, sort=sort)
assert inter is first
