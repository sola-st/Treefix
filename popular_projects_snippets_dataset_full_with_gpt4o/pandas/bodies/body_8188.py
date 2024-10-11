# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
dr = bdate_range("1/1/2009", "1/1/2010")
dr_utc = bdate_range("1/1/2009", "1/1/2010", tz=pytz.utc)
localized = dr.tz_localize(pytz.utc)
tm.assert_index_equal(dr_utc, localized)
