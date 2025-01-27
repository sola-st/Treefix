# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_scalar_compat.py
dti = date_range("20130101 09:10:11", periods=5)
result = dti.round("D")
expected = date_range("20130101", periods=5)
tm.assert_index_equal(result, expected)

dti = dti.tz_localize("UTC").tz_convert("US/Eastern")
result = dti.round("D")
expected = date_range("20130101", periods=5).tz_localize("US/Eastern")
tm.assert_index_equal(result, expected)

result = dti.round("s")
tm.assert_index_equal(result, dti)
