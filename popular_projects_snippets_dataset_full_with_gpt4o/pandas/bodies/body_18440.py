# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
dti = date_range("2016-01-01", periods=3, tz=tz_naive_fixture)
expected = dti - dti

obj = tm.box_expected(dti, box_with_array)
expected = tm.box_expected(expected, box_with_array).astype(object)

with tm.assert_produces_warning(PerformanceWarning):
    result = obj - obj.astype(object)
tm.assert_equal(result, expected)
