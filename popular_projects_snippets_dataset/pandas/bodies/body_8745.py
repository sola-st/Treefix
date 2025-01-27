# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
# Case where infer_freq inside would choose "D" instead of "B"
dta = pd.date_range("2021-10-18", periods=3, freq="B")._data
parr = dta.to_period()
result = parr.to_timestamp()
assert result.freq == "B"
tm.assert_extension_array_equal(result, dta)

dta2 = dta[::2]
parr2 = dta2.to_period()
result2 = parr2.to_timestamp()
assert result2.freq == "2B"
tm.assert_extension_array_equal(result2, dta2)

parr3 = dta.to_period("2B")
result3 = parr3.to_timestamp()
assert result3.freq == "B"
tm.assert_extension_array_equal(result3, dta)
