# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# Check that DatetimeArray defers to Index classes
dti = date_range("20130101", periods=3, tz=tz_naive_fixture)
dta = dti.array
result = dta - dti
expected = dti - dti
tm.assert_index_equal(result, expected)

tdi = result
result = dta + tdi
expected = dti + tdi
tm.assert_index_equal(result, expected)

result = dta - tdi
expected = dti - tdi
tm.assert_index_equal(result, expected)
