# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
values = [1, 2, 3 + 1j]
c1 = Categorical(values)
tm.assert_index_equal(c1.categories, Index(values))
tm.assert_numpy_array_equal(np.array(c1), np.array(values))
