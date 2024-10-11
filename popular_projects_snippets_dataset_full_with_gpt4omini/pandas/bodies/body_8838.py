# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
dta, dti = dta_dti

result = dta.to_pydatetime()
expected = dti.to_pydatetime()
tm.assert_numpy_array_equal(result, expected)
