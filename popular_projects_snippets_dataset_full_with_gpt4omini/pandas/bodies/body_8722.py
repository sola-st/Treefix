# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
arr = arr1d
dti = self.index_cls(arr1d)
assert list(dti) == list(arr)

# Check that Index.__new__ knows what to do with DatetimeArray
dti2 = pd.Index(arr)
assert isinstance(dti2, DatetimeIndex)
assert list(dti2) == list(arr)
