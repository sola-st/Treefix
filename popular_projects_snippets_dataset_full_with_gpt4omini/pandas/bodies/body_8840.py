# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
# In this case we should get the same formatted values with our nano
#  version dti._data as we do with the non-nano dta
dta, dti = dta_dti

res = dta._format_native_types()
exp = dti._data._format_native_types()
tm.assert_numpy_array_equal(res, exp)
