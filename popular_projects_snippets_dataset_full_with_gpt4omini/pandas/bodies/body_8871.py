# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
dti = pd.date_range("1994-05-12", periods=12, tz="US/Pacific")
dta = dti._data.reshape(3, 4)
result = dta.tz_localize(None)

expected = dta.ravel().tz_localize(None).reshape(dta.shape)
tm.assert_datetime_array_equal(result, expected)

roundtrip = expected.tz_localize("US/Pacific")
tm.assert_datetime_array_equal(roundtrip, dta)
