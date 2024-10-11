# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
sc = ser.copy()
result = ser.replace(to_rep, val)
return_value = sc.replace(to_rep, val, inplace=True)
assert return_value is None
tm.assert_series_equal(expected, result)
tm.assert_series_equal(expected, sc)
