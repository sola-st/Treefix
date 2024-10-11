# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_set_index.py
ci = tm.makeCategoricalIndex(10)
ci.name = "B"

# with Categorical
df = DataFrame({"A": np.random.randn(10), "B": ci.values})
idf = df.set_index("B")
tm.assert_index_equal(idf.index, ci)

# from a CategoricalIndex
df = DataFrame({"A": np.random.randn(10), "B": ci})
idf = df.set_index("B")
tm.assert_index_equal(idf.index, ci)

# round-trip
idf = idf.reset_index().set_index("B")
tm.assert_index_equal(idf.index, ci)
