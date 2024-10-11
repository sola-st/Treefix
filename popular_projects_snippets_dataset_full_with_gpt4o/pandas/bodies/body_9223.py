# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_operators.py
# https://github.com/pandas-dev/pandas/issues/26504
# and following comparisons of missing values in ordered Categorical
# with listlike should be evaluated as False

cat = Categorical([1, 2, 3, None], categories=[1, 2, 3], ordered=True)
other = Categorical([2, 2, 2, 2], categories=[1, 2, 3], ordered=True)
with warnings.catch_warnings():
    warnings.simplefilter("ignore", RuntimeWarning)
    expected = getattr(np.array(cat), compare_operators_no_eq_ne)(2)
actual = getattr(cat, compare_operators_no_eq_ne)(other)
tm.assert_numpy_array_equal(actual, expected)
