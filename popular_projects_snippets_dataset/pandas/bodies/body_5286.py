# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
cases = {
    "M": ["MTH", "MONTH", "MONTHLY", "Mth", "month", "monthly"],
    "B": ["BUS", "BUSINESS", "BUSINESSLY", "WEEKDAY", "bus"],
    "D": ["DAY", "DLY", "DAILY", "Day", "Dly", "Daily"],
    "H": ["HR", "HOUR", "HRLY", "HOURLY", "hr", "Hour", "HRly"],
    "T": ["minute", "MINUTE", "MINUTELY", "minutely"],
    "S": ["sec", "SEC", "SECOND", "SECONDLY", "second"],
    "L": ["MILLISECOND", "MILLISECONDLY", "millisecond"],
    "U": ["MICROSECOND", "MICROSECONDLY", "microsecond"],
    "N": ["NANOSECOND", "NANOSECONDLY", "nanosecond"],
}

msg = INVALID_FREQ_ERR_MSG
for exp, freqs in cases.items():
    for freq in freqs:
        with pytest.raises(ValueError, match=msg):
            Period("2016-03-01 09:00", freq=freq)
        with pytest.raises(ValueError, match=msg):
            Period(ordinal=1, freq=freq)

            # check supported freq-aliases still works
    p1 = Period("2016-03-01 09:00", freq=exp)
    p2 = Period(ordinal=1, freq=exp)
    assert isinstance(p1, Period)
    assert isinstance(p2, Period)
