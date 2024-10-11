# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_indexing.py

# GH 9469
# properly coerce the input indexers
np.random.seed(1)
c = Categorical(np.random.randint(0, 5, size=150000).astype(np.int8))
result = c.codes[np.array([100000]).astype(np.int64)]
expected = c[np.array([100000]).astype(np.int64)].codes
tm.assert_numpy_array_equal(result, expected)
