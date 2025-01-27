# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
s = Series(np.random.rand(10))
df = DataFrame(s, index=np.arange(len(s)))
i = Series(np.arange(10), name="iname")

df = df.reindex(i)
assert df.index.name == "iname"

df = df.reindex(Index(np.arange(10), name="tmpname"))
assert df.index.name == "tmpname"

s = Series(np.random.rand(10))
df = DataFrame(s.T, index=np.arange(len(s)))
i = Series(np.arange(10), name="iname")
df = df.reindex(columns=i)
assert df.columns.name == "iname"
