# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_ops.py
t1 = rng.copy()
t2 = rng.copy()
assert t1.identical(t2)

# name
t1 = t1.rename("foo")
assert t1.equals(t2)
assert not t1.identical(t2)
t2 = t2.rename("foo")
assert t1.identical(t2)

# freq
t2v = Index(t2.values)
assert t1.equals(t2v)
assert not t1.identical(t2v)
