# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_drop_duplicates.py
# no unused categories, unlike cat_series_unused_category
cat_array = np.array([1, 2, 3, 4, 5], dtype=np.dtype(dtype))

input2 = np.array([1, 2, 3, 5, 3, 2, 4], dtype=np.dtype(dtype))
cat = Categorical(input2, categories=cat_array, ordered=ordered)
tc2 = Series(cat)
exit(tc2)
