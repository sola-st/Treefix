# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
dti = pd.date_range("2016-01-01", periods=3)
dta = dti._data.as_unit("us")

ts = dta[0].as_unit("s")

result = dta - ts
expected = (dti - dti[0])._data.as_unit("us")
assert result.dtype == "m8[us]"
tm.assert_extension_array_equal(result, expected)
