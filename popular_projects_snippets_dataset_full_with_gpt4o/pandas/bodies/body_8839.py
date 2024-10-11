# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
dta, dti = dta_dti

result = getattr(dta, meth)
expected = getattr(dti, meth)
tm.assert_numpy_array_equal(result, expected)
