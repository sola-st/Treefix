# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
box = box_with_array
dti = pd.date_range("2016-01-01", periods=3)
tdi = dti - dti.shift(1)
tdarr = tdi.values

expected = 2 * tdi
tdi = tm.box_expected(tdi, box)
expected = tm.box_expected(expected, box)

result = tdi + tdarr
tm.assert_equal(result, expected)
result = tdarr + tdi
tm.assert_equal(result, expected)

expected_sub = 0 * tdi
result = tdi - tdarr
tm.assert_equal(result, expected_sub)
result = tdarr - tdi
tm.assert_equal(result, expected_sub)
