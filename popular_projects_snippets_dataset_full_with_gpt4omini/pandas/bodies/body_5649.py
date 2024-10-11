# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
assert case.is_unique is True
tm.assert_numpy_array_equal(case.duplicated(), np.array([False, False, False]))
