# Extracted from ./data/repos/pandas/pandas/tests/series/test_repr.py
s = Series([1, 2, 3], name=np.int64(3))

# it works!
repr(s)

s.name = ("\u05d0",) * 2
repr(s)
