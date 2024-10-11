# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
dti = pd.date_range("2016-01-01", periods=3)

dta = dti._data
expected = DatetimeArray(np.roll(dta._ndarray, 1))

fv = dta[-1]
for fill_value in [fv, fv.to_pydatetime(), fv.to_datetime64()]:
    result = dta.shift(1, fill_value=fill_value)
    tm.assert_datetime_array_equal(result, expected)

dta = dta.tz_localize("UTC")
expected = expected.tz_localize("UTC")
fv = dta[-1]
for fill_value in [fv, fv.to_pydatetime()]:
    result = dta.shift(1, fill_value=fill_value)
    tm.assert_datetime_array_equal(result, expected)
