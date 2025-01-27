# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
expecteds = {
    "BusinessDay": Timestamp("2010-12-31 09:00:00"),
    "CustomBusinessDay": Timestamp("2010-12-31 09:00:00"),
    "CustomBusinessMonthEnd": Timestamp("2010-12-31 09:00:00"),
    "CustomBusinessMonthBegin": Timestamp("2010-12-01 09:00:00"),
    "BusinessMonthBegin": Timestamp("2010-12-01 09:00:00"),
    "MonthEnd": Timestamp("2010-12-31 09:00:00"),
    "SemiMonthEnd": Timestamp("2010-12-31 09:00:00"),
    "BusinessMonthEnd": Timestamp("2010-12-31 09:00:00"),
    "BYearBegin": Timestamp("2010-01-01 09:00:00"),
    "YearEnd": Timestamp("2010-12-31 09:00:00"),
    "BYearEnd": Timestamp("2010-12-31 09:00:00"),
    "QuarterBegin": Timestamp("2010-12-01 09:00:00"),
    "BQuarterBegin": Timestamp("2010-12-01 09:00:00"),
    "QuarterEnd": Timestamp("2010-12-31 09:00:00"),
    "BQuarterEnd": Timestamp("2010-12-31 09:00:00"),
    "BusinessHour": Timestamp("2010-12-31 17:00:00"),
    "CustomBusinessHour": Timestamp("2010-12-31 17:00:00"),
    "WeekOfMonth": Timestamp("2010-12-11 09:00:00"),
    "LastWeekOfMonth": Timestamp("2010-12-25 09:00:00"),
    "FY5253Quarter": Timestamp("2010-10-26 09:00:00"),
    "FY5253": Timestamp("2010-01-26 09:00:00"),
    "Easter": Timestamp("2010-04-04 09:00:00"),
}

# result will not be changed if the target is on the offset
for n in [
    "Day",
    "MonthBegin",
    "SemiMonthBegin",
    "YearBegin",
    "Week",
    "Hour",
    "Minute",
    "Second",
    "Milli",
    "Micro",
    "Nano",
    "DateOffset",
]:
    expecteds[n] = Timestamp("2011/01/01 09:00")

# but be changed when normalize=True
norm_expected = expecteds.copy()
for k in norm_expected:
    norm_expected[k] = Timestamp(norm_expected[k].date())

normalized = {
    "Day": Timestamp("2010-12-31 00:00:00"),
    "DateOffset": Timestamp("2010-12-31 00:00:00"),
    "MonthBegin": Timestamp("2010-12-01 00:00:00"),
    "SemiMonthBegin": Timestamp("2010-12-15 00:00:00"),
    "YearBegin": Timestamp("2010-01-01 00:00:00"),
    "Week": Timestamp("2010-12-25 00:00:00"),
    "Hour": Timestamp("2011-01-01 00:00:00"),
    "Minute": Timestamp("2011-01-01 00:00:00"),
    "Second": Timestamp("2011-01-01 00:00:00"),
    "Milli": Timestamp("2011-01-01 00:00:00"),
    "Micro": Timestamp("2011-01-01 00:00:00"),
}
norm_expected.update(normalized)

sdt = datetime(2011, 1, 1, 9, 0)
ndt = np.datetime64("2011-01-01 09:00")

for dt in [sdt, ndt]:
    expected = expecteds[offset_types.__name__]
    self._check_offsetfunc_works(offset_types, "rollback", dt, expected)

    expected = norm_expected[offset_types.__name__]
    self._check_offsetfunc_works(
        offset_types, "rollback", dt, expected, normalize=True
    )
