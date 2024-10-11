# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
dti = DatetimeIndex(
    [
        Timestamp("2000-01-05 00:15:00"),
        Timestamp("2000-01-31 00:23:00"),
        Timestamp("2000-01-01"),
        Timestamp("2000-02-29"),
        Timestamp("2000-12-31"),
    ]
)
actual = DatetimeIndex(shift_months(dti.asi8, years * 12 + months))

raw = [x + pd.offsets.DateOffset(years=years, months=months) for x in dti]
expected = DatetimeIndex(raw)
tm.assert_index_equal(actual, expected)
