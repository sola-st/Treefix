# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
result = Categorical(
    [Interval(1, 2), Interval(2, 3), Interval(3, 6)], ordered=True
)
ii = IntervalIndex([Interval(1, 2), Interval(2, 3), Interval(3, 6)])
exp = Categorical(ii, ordered=True)
tm.assert_categorical_equal(result, exp)
tm.assert_index_equal(result.categories, ii)
