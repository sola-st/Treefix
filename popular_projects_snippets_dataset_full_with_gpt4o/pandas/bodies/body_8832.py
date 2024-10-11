# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
dti = pd.date_range("2016-01-01 06:00:00", periods=55, freq="D")
arr = np.asarray(dti).astype(f"M8[{unit}]")

dta = DatetimeArray._simple_new(arr, dtype=arr.dtype)

assert not dta.is_normalized

# TODO: simplify once we can just .astype to other unit
exp = np.asarray(dti.normalize()).astype(f"M8[{unit}]")
expected = DatetimeArray._simple_new(exp, dtype=exp.dtype)

res = dta.normalize()
tm.assert_extension_array_equal(res, expected)
