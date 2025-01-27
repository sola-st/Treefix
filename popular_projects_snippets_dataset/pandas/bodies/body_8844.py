# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
dta, dti = dta_dti

td = pd.Timedelta(scalar)
exp_reso = max(dta._creso, td._creso)
exp_unit = npy_unit_to_abbrev(exp_reso)

expected = (dti + td)._data.as_unit(exp_unit)
result = dta + scalar
tm.assert_extension_array_equal(result, expected)

result = scalar + dta
tm.assert_extension_array_equal(result, expected)

expected = (dti - td)._data.as_unit(exp_unit)
result = dta - scalar
tm.assert_extension_array_equal(result, expected)
