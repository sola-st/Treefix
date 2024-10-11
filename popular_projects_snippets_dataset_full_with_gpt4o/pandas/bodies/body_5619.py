# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
vals = np.array([0, 1, 2, 0])
cats = ["a", "b", "c"]
cat = Categorical([1]).from_codes(vals, cats)
other = Categorical([1]).from_codes(np.array([0, 1]), cats)

expected = np.array([True, True, False, True])
result = algos.isin(cat, other)
tm.assert_numpy_array_equal(expected, result)
