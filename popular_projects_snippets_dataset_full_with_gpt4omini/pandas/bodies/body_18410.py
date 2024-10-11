# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
tz = tz_naive_fixture

dta = date_range("1970-01-01", freq="ns", periods=10, tz=tz)._data
obj = tm.box_expected(dta, box_with_array)
assert_invalid_comparison(obj, other, box_with_array)
