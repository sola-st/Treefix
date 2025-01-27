# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_missing.py
# #1457

categories = list(range(10))
labels = np.random.randint(0, 10, 20)
labels[::5] = -1

cat = Categorical(labels, categories, fastpath=True)
repr(cat)

tm.assert_numpy_array_equal(isna(cat), labels == -1)
