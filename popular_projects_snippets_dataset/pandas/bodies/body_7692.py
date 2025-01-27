# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_constructors.py
# GH#15286 passing read-only array to from_product
a = np.array(range(3))
b = ["a", "b"]
expected = MultiIndex.from_product([a, b])

a.setflags(write=False)
result = MultiIndex.from_product([a, b])
tm.assert_index_equal(result, expected)
