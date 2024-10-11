# Extracted from ./data/repos/pandas/pandas/tests/arrays/interval/test_interval.py
# GH#31502, GH#31504
a = IntervalArray.from_breaks(date_range("2000", periods=4))
result = a.shift(2)
expected = a.take([-1, -1, 0], allow_fill=True)
tm.assert_interval_array_equal(result, expected)

result = a.shift(-1)
expected = a.take([1, 2, -1], allow_fill=True)
tm.assert_interval_array_equal(result, expected)
