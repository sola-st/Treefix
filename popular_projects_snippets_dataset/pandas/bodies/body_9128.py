# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_algos.py
cat = pd.Categorical(
    ["b", "b", None, "a"], categories=["c", "b", "a"], ordered=True
)

codes, uniques = pd.factorize(cat, sort=True)
expected_codes = np.array([0, 0, -1, 1], dtype=np.intp)
expected_uniques = pd.Categorical(
    ["b", "a"], categories=["c", "b", "a"], ordered=True
)

tm.assert_numpy_array_equal(codes, expected_codes)
tm.assert_categorical_equal(uniques, expected_uniques)
