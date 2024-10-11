# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
dta, dti = dta_dti
result = dta.to_period("D")
expected = dti._data.to_period("D")

tm.assert_extension_array_equal(result, expected)
