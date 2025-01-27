# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_indexing.py

# GH#9469
# properly coerce the input indexers
np.random.seed(1)
cat = Categorical(
    np.random.randint(0, 5, size=150000).astype(np.int8)
).add_categories([-1000])
indexer = np.array([100000]).astype(np.int64)
cat[indexer] = -1000

# we are asserting the code result here
# which maps to the -1000 category
result = cat.codes[np.array([100000]).astype(np.int64)]
tm.assert_numpy_array_equal(result, np.array([5], dtype="int8"))
