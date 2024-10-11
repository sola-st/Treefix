# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
pi = self.index_cls(arr1d)
arr = arr1d

expected = DatetimeArray(pi.to_timestamp(how=how))
result = arr.to_timestamp(how=how)
assert isinstance(result, DatetimeArray)

# placeholder until these become actual EA subclasses and we can use
#  an EA-specific tm.assert_ function
tm.assert_index_equal(pd.Index(result), pd.Index(expected))
