# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_setops.py
first = tm.makeDateIndex(10)
second = first[5:]
intersect = first.intersection(second)
assert tm.equalContents(intersect, second)

# GH 10149
cases = [klass(second.values) for klass in [np.array, Series, list]]
for case in cases:
    result = first.intersection(case)
    assert tm.equalContents(result, second)

third = Index(["a", "b", "c"])
result = first.intersection(third)
expected = Index([], dtype=object)
tm.assert_index_equal(result, expected)
