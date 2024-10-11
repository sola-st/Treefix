# Extracted from ./data/repos/pandas/pandas/tests/arrays/interval/test_interval.py
# https://github.com/pandas-dev/pandas/issues/31495, GH#22428, GH#31502
a = IntervalArray.from_breaks([1, 2, 3])
result = a.shift()
# int -> float
expected = IntervalArray.from_tuples([(np.nan, np.nan), (1.0, 2.0)])
tm.assert_interval_array_equal(result, expected)
