# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
expecteds = expecteds.copy()

# result will not be changed if the target is on the offset
no_changes = [
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
]
for n in no_changes:
    expecteds[n] = Timestamp("2011/01/01 09:00")

expecteds["BusinessHour"] = Timestamp("2011-01-03 09:00:00")
expecteds["CustomBusinessHour"] = Timestamp("2011-01-03 09:00:00")

# but be changed when normalize=True
norm_expected = expecteds.copy()
for k in norm_expected:
    norm_expected[k] = Timestamp(norm_expected[k].date())

normalized = {
    "Day": Timestamp("2011-01-02 00:00:00"),
    "DateOffset": Timestamp("2011-01-02 00:00:00"),
    "MonthBegin": Timestamp("2011-02-01 00:00:00"),
    "SemiMonthBegin": Timestamp("2011-01-15 00:00:00"),
    "YearBegin": Timestamp("2012-01-01 00:00:00"),
    "Week": Timestamp("2011-01-08 00:00:00"),
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
    self._check_offsetfunc_works(offset_types, "rollforward", dt, expected)
    expected = norm_expected[offset_types.__name__]
    self._check_offsetfunc_works(
        offset_types, "rollforward", dt, expected, normalize=True
    )
