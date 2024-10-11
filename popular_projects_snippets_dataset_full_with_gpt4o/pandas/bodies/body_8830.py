# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
arr = np.arange(5, dtype=np.int64).view(f"M8[{unit}]")
dta = DatetimeArray._simple_new(arr, dtype=dtype)

assert dta.dtype == dtype
assert dta[0].unit == unit
assert tz_compare(dta.tz, dta[0].tz)
assert (dta[0] == dta[:1]).all()
