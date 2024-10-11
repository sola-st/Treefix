# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_operators.py
# GH8658
cat = Categorical([1, 2, 3], ordered=True)
tm.assert_numpy_array_equal(cat > cat[0], np.array([False, True, True]))
tm.assert_numpy_array_equal(cat[0] < cat, np.array([False, True, True]))
