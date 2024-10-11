# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
index = Index(tm.rands_array(10, 100))

values = Series(np.random.randn(50), index=index[::2])
labels = np.random.randint(0, 5, 50)

# it works!
grouped = values.groupby(labels)

# accessing the index elements causes segfault
f = lambda x: len(set(map(id, x.index)))
grouped.agg(f)
