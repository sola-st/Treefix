# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py
hcal = USFederalHolidayCalendar()
cbmb = CBMonthBegin(calendar=hcal)
assert date_range(start="20120101", end="20130101", freq=cbmb).tolist()[
    0
] == datetime(2012, 1, 3)
