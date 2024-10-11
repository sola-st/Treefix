# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# Anything but object and we get all-False shortcut

dta = date_range("2013-01-01", periods=3)._values
if dtype1 == "period[D]":
    # TODO: fix Series.view to get this on its own
    arr = dta.to_period("D")
elif dtype1 == "M8[ns, UTC]":
    # TODO: fix Series.view to get this on its own
    arr = dta.tz_localize("UTC")
else:
    arr = Series(dta.view("i8")).view(dtype1)._values

comps = arr.view("i8").astype(dtype)

result = algos.isin(comps, arr)
expected = np.zeros(comps.shape, dtype=bool)
tm.assert_numpy_array_equal(result, expected)
