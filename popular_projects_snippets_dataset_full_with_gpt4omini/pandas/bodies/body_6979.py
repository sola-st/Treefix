# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
# GH#10149
first = index[5:20]
second = index[:10]
everything = index[:20]

case = klass(second.values)
result = first.union(case, sort=sort)
if sort is None:
    tm.assert_index_equal(result, everything.sort_values())
assert tm.equalContents(result, everything)
