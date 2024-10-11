# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py

a = np.random.randint(1, 1 << 10, 1 << 15).astype(np.intp)

left = ht.unique_label_indices(a)
right = np.unique(a, return_index=True)[1]

tm.assert_numpy_array_equal(left, right, check_dtype=False)

a[np.random.choice(len(a), 10)] = -1
left = ht.unique_label_indices(a)
right = np.unique(a, return_index=True)[1][1:]
tm.assert_numpy_array_equal(left, right, check_dtype=False)
