# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_day.py

dti = DatetimeIndex([dt])
expected = DatetimeIndex([datetime(2008, 1, 2, 2)])

result = dti + (td + offset)
tm.assert_index_equal(result, expected)

result = dti + (offset + td)
tm.assert_index_equal(result, expected)
