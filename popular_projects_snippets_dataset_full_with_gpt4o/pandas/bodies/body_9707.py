# Extracted from ./data/repos/pandas/pandas/tests/arrays/datetimes/test_constructors.py
dtype = DatetimeTZDtype(tz="US/Central")
arr = DatetimeArray._from_sequence(["2000"], dtype=dtype)
result = DatetimeArray._from_sequence_not_strict(arr, dtype=dtype)
tm.assert_equal(arr, result)
