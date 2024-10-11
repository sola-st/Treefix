# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
# freq is DateOffset
msg = "|".join(
    [
        "Input has different freq",
        "Input cannot be converted to Period",
    ]
)

for freq in ["A", "2A", "3A"]:
    p = Period("2011", freq=freq)
    assert p - offsets.YearEnd(2) == Period("2009", freq=freq)

    for o in [
        offsets.YearBegin(2),
        offsets.MonthBegin(1),
        offsets.Minute(),
        np.timedelta64(365, "D"),
        timedelta(365),
    ]:
        with pytest.raises(IncompatibleFrequency, match=msg):
            p - o

for freq in ["M", "2M", "3M"]:
    p = Period("2011-03", freq=freq)
    assert p - offsets.MonthEnd(2) == Period("2011-01", freq=freq)
    assert p - offsets.MonthEnd(12) == Period("2010-03", freq=freq)

    for o in [
        offsets.YearBegin(2),
        offsets.MonthBegin(1),
        offsets.Minute(),
        np.timedelta64(365, "D"),
        timedelta(365),
    ]:
        with pytest.raises(IncompatibleFrequency, match=msg):
            p - o

        # freq is Tick
for freq in ["D", "2D", "3D"]:
    p = Period("2011-04-01", freq=freq)
    assert p - offsets.Day(5) == Period("2011-03-27", freq=freq)
    assert p - offsets.Hour(24) == Period("2011-03-31", freq=freq)
    assert p - np.timedelta64(2, "D") == Period("2011-03-30", freq=freq)
    assert p - np.timedelta64(3600 * 24, "s") == Period("2011-03-31", freq=freq)
    assert p - timedelta(-2) == Period("2011-04-03", freq=freq)
    assert p - timedelta(hours=48) == Period("2011-03-30", freq=freq)

    for o in [
        offsets.YearBegin(2),
        offsets.MonthBegin(1),
        offsets.Minute(),
        np.timedelta64(4, "h"),
        timedelta(hours=23),
    ]:
        with pytest.raises(IncompatibleFrequency, match=msg):
            p - o

for freq in ["H", "2H", "3H"]:
    p = Period("2011-04-01 09:00", freq=freq)
    assert p - offsets.Day(2) == Period("2011-03-30 09:00", freq=freq)
    assert p - offsets.Hour(3) == Period("2011-04-01 06:00", freq=freq)
    assert p - np.timedelta64(3, "h") == Period("2011-04-01 06:00", freq=freq)
    assert p - np.timedelta64(3600, "s") == Period(
        "2011-04-01 08:00", freq=freq
    )
    assert p - timedelta(minutes=120) == Period("2011-04-01 07:00", freq=freq)
    assert p - timedelta(days=4, minutes=180) == Period(
        "2011-03-28 06:00", freq=freq
    )

    for o in [
        offsets.YearBegin(2),
        offsets.MonthBegin(1),
        offsets.Minute(),
        np.timedelta64(3200, "s"),
        timedelta(hours=23, minutes=30),
    ]:
        with pytest.raises(IncompatibleFrequency, match=msg):
            p - o
