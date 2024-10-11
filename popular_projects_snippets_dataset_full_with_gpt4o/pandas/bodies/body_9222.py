# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_operators.py
# https://github.com/pandas-dev/pandas/issues/26504
# BUG: fix ordered categorical comparison with missing values (#26504 )
# and following comparisons with scalars in categories with missing
# values should be evaluated as False

cat = Categorical([1, 2, 3, None], categories=[1, 2, 3], ordered=True)
scalar = 2
with warnings.catch_warnings():
    warnings.simplefilter("ignore", RuntimeWarning)
    expected = getattr(np.array(cat), compare_operators_no_eq_ne)(scalar)
actual = getattr(cat, compare_operators_no_eq_ne)(scalar)
tm.assert_numpy_array_equal(actual, expected)
