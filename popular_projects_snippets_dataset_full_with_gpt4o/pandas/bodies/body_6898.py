# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_setops.py
# GH 10149
index = Index([0, "a", 1, "b", 2, "c"])
first = index[3:]
second = index[:5]

result = first.union(klass(second.values))

assert tm.equalContents(result, index)
