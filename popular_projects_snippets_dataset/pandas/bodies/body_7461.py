# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_setops.py
other = Index(["A", "B", "C"])

result = other.union(idx)
assert ("foo", "one") in result
assert "B" in result

msg = "The values in the array are unorderable"
with tm.assert_produces_warning(RuntimeWarning, match=msg):
    result2 = idx.union(other)
# This is more consistent now, if sorting fails then we don't sort at all
# in the MultiIndex case.
assert not result.equals(result2)
