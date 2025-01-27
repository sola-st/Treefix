# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_index.py
A = np.arange(20).repeat(5)
B = np.tile(np.arange(5), 20)

indexer = np.random.permutation(100)
A = A.take(indexer)
B = B.take(indexer)

df = DataFrame({"A": A, "B": B, "C": np.random.randn(100)})

ex_indexer = np.lexsort((df.B.max() - df.B, df.A))
expected = df.take(ex_indexer)

# test with multiindex, too
idf = df.set_index(["A", "B"])

result = idf.sort_index(ascending=[1, 0])
expected = idf.take(ex_indexer)
tm.assert_frame_equal(result, expected)

# also, Series!
result = idf["C"].sort_index(ascending=[1, 0])
tm.assert_series_equal(result, expected["C"])
