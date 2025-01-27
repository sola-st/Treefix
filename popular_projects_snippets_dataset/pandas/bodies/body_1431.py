# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
df = DataFrame({"a": [0, 1], "b": [2, 3]})
for name in ("loc", "iloc", "at", "iat"):
    getattr(df, name)
wr = weakref.ref(df)
del df
assert wr() is None
