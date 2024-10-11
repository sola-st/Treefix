# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
# GH #331
a = DataFrame(np.random.randn(30, 2), columns=["a", "b"])
c = Series(np.random.randn(30))
a["c"] = c
d = DataFrame(np.random.randn(30, 1), columns=["q"])

# it works!
a.join(d)
d.join(a)
