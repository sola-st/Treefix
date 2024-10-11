# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
idx = pd.interval_range(0, 10, periods=10)
cat = Categorical(idx, categories=idx)
expected_codes = np.arange(10, dtype="int8")
tm.assert_numpy_array_equal(cat.codes, expected_codes)
tm.assert_index_equal(cat.categories, idx)

# infer categories
cat = Categorical(idx)
tm.assert_numpy_array_equal(cat.codes, expected_codes)
tm.assert_index_equal(cat.categories, idx)

# list values
cat = Categorical(list(idx))
tm.assert_numpy_array_equal(cat.codes, expected_codes)
tm.assert_index_equal(cat.categories, idx)

# list values, categories
cat = Categorical(list(idx), categories=list(idx))
tm.assert_numpy_array_equal(cat.codes, expected_codes)
tm.assert_index_equal(cat.categories, idx)

# shuffled
values = idx.take([1, 2, 0])
cat = Categorical(values, categories=idx)
tm.assert_numpy_array_equal(cat.codes, np.array([1, 2, 0], dtype="int8"))
tm.assert_index_equal(cat.categories, idx)

# extra
values = pd.interval_range(8, 11, periods=3)
cat = Categorical(values, categories=idx)
expected_codes = np.array([8, 9, -1], dtype="int8")
tm.assert_numpy_array_equal(cat.codes, expected_codes)
tm.assert_index_equal(cat.categories, idx)

# overlapping
idx = IntervalIndex([Interval(0, 2), Interval(0, 1)])
cat = Categorical(idx, categories=idx)
expected_codes = np.array([0, 1], dtype="int8")
tm.assert_numpy_array_equal(cat.codes, expected_codes)
tm.assert_index_equal(cat.categories, idx)
