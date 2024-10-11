# Extracted from ./data/repos/pandas/pandas/tests/arrays/interval/test_interval.py
# GH 21670
array = IntervalArray.from_breaks(range(10), closed=closed)
result = array.set_closed(new_closed)
expected = IntervalArray.from_breaks(range(10), closed=new_closed)
tm.assert_extension_array_equal(result, expected)
