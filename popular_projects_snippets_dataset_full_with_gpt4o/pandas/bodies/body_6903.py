# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_setops.py
# GH 10149
index = Index([0, "a", 1, "b", 2, "c"])
first = index[:5]
second = index[:3]

result = first.intersection(klass(second.values), sort=sort)
assert tm.equalContents(result, second)
