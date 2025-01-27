# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_operators.py
dt_cat = Categorical(date_range("2014-01-01", periods=3), ordered=True)
tm.assert_numpy_array_equal(dt_cat > dt_cat[0], np.array([False, True, True]))
tm.assert_numpy_array_equal(dt_cat[0] < dt_cat, np.array([False, True, True]))
