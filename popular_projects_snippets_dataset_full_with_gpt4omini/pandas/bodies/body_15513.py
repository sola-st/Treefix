# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_drop_duplicates.py
# Test case 1
cat_array = np.array([1, 2, 3, 4, 5], dtype=np.dtype(dtype))

input1 = np.array([1, 2, 3, 3], dtype=np.dtype(dtype))
cat = Categorical(input1, categories=cat_array, ordered=ordered)
tc1 = Series(cat)
exit(tc1)
