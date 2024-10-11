# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
arr = np.arange(5, dtype=np.int64).view(f"M8[{unit}]")
dtype = DatetimeTZDtype(unit, "UTC")

dta = DatetimeArray._simple_new(arr, dtype=dtype)
assert dta.dtype == dtype

wrong = DatetimeTZDtype("ns", "UTC")
with pytest.raises(AssertionError, match=""):
    DatetimeArray._simple_new(arr, dtype=wrong)
