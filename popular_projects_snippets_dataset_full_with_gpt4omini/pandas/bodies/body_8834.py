# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
dti = pd.date_range("2016-01-01", periods=55, freq="D")
arr = np.asarray(dti).astype(f"M8[{unit}]")

dta = DatetimeArray._simple_new(arr, dtype=arr.dtype)

# we should match the nano-reso std, but floored to our reso.
res = dta.std()
assert res._creso == dta._creso
assert res == dti.std().floor(unit)
