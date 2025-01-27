# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_missing.py
exp = np.array([False, False, True])
cat = Categorical(["a", "b", np.nan])
res = cat.isna()

tm.assert_numpy_array_equal(res, exp)
