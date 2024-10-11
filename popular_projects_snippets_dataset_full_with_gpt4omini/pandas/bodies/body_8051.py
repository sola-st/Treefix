# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py

# index
i1 = Index(["a", "b", "c"])
i2 = Index(["a", "b", "c"])

assert i1.identical(i2)

i1 = i1.rename("foo")
assert i1.equals(i2)
assert not i1.identical(i2)

i2 = i2.rename("foo")
assert i1.identical(i2)

i3 = Index([("a", "a"), ("a", "b"), ("b", "a")])
i4 = Index([("a", "a"), ("a", "b"), ("b", "a")], tupleize_cols=False)
assert not i3.identical(i4)
