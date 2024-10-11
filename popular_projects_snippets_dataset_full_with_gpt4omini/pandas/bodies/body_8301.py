# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_setops.py
everything = tm.makeDateIndex(10)
first = everything[:5]
second = everything[5:]

# GH 10149 support listlike inputs other than Index objects
expected = first.union(second, sort=sort)
case = box(second.values)
result = first.union(case, sort=sort)
tm.assert_index_equal(result, expected)
