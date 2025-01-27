# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
dti = datetime_index
arr = DatetimeArray(dti)

expected = dti.to_period(freq=freqstr)
result = arr.to_period(freq=freqstr)
assert isinstance(result, PeriodArray)

# placeholder until these become actual EA subclasses and we can use
#  an EA-specific tm.assert_ function
tm.assert_index_equal(pd.Index(result), pd.Index(expected))
