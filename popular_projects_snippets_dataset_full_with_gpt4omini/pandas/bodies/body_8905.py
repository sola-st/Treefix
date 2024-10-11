# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_arithmetics.py
# We have to use tm.assert_sp_array_equal. See GH #45126
tm.assert_numpy_array_equal(a, b)
