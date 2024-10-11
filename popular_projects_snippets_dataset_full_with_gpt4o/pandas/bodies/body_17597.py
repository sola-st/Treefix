# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_custom_business_day.py
weekmask_egypt = "Sun Mon Tue Wed Thu"  # Fri-Sat Weekend
holidays = ["2012-05-01", datetime(2013, 5, 1), np.datetime64("2014-05-01")]
bday_egypt = CDay(holidays=holidays, weekmask=weekmask_egypt)
dt = datetime(2013, 4, 30)
xp_egypt = datetime(2013, 5, 5)
assert xp_egypt == dt + 2 * bday_egypt
