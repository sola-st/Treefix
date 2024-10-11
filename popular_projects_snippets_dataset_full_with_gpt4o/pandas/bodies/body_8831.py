# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
dta, dti = dta_dti

assert (dti == dta).all()

res = getattr(dta, field)
expected = getattr(dti._data, field)
tm.assert_numpy_array_equal(res, expected)
