# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
# freq is DateOffset
for freq in ["A", "2A", "3A"]:
    p = Period("2011", freq=freq)
    exp = Period("2013", freq=freq)
    assert p + offsets.YearEnd(2) == exp
    assert offsets.YearEnd(2) + p == exp

    for o in [
        offsets.YearBegin(2),
        offsets.MonthBegin(1),
        offsets.Minute(),
        np.timedelta64(365, "D"),
        timedelta(365),
    ]:
        msg = "Input has different freq|Input cannot be converted to Period"
        with pytest.raises(IncompatibleFrequency, match=msg):
            p + o
        with pytest.raises(IncompatibleFrequency, match=msg):
            o + p

for freq in ["M", "2M", "3M"]:
    p = Period("2011-03", freq=freq)
    exp = Period("2011-05", freq=freq)
    assert p + offsets.MonthEnd(2) == exp
    assert offsets.MonthEnd(2) + p == exp

    exp = Period("2012-03", freq=freq)
    assert p + offsets.MonthEnd(12) == exp
    assert offsets.MonthEnd(12) + p == exp

    msg = "|".join(
        [
            "Input has different freq",
            "Input cannot be converted to Period",
        ]
    )

    for o in [
        offsets.YearBegin(2),
        offsets.MonthBegin(1),
        offsets.Minute(),
        np.timedelta64(365, "D"),
        timedelta(365),
    ]:

        with pytest.raises(IncompatibleFrequency, match=msg):
            p + o
        with pytest.raises(IncompatibleFrequency, match=msg):
            o + p

        # freq is Tick
for freq in ["D", "2D", "3D"]:
    p = Period("2011-04-01", freq=freq)

    exp = Period("2011-04-06", freq=freq)
    assert p + offsets.Day(5) == exp
    assert offsets.Day(5) + p == exp

    exp = Period("2011-04-02", freq=freq)
    assert p + offsets.Hour(24) == exp
    assert offsets.Hour(24) + p == exp

    exp = Period("2011-04-03", freq=freq)
    assert p + np.timedelta64(2, "D") == exp
    assert np.timedelta64(2, "D") + p == exp

    exp = Period("2011-04-02", freq=freq)
    assert p + np.timedelta64(3600 * 24, "s") == exp
    assert np.timedelta64(3600 * 24, "s") + p == exp

    exp = Period("2011-03-30", freq=freq)
    assert p + timedelta(-2) == exp
    assert timedelta(-2) + p == exp

    exp = Period("2011-04-03", freq=freq)
    assert p + timedelta(hours=48) == exp
    assert timedelta(hours=48) + p == exp

    msg = "|".join(
        [
            "Input has different freq",
            "Input cannot be converted to Period",
        ]
    )

    for o in [
        offsets.YearBegin(2),
        offsets.MonthBegin(1),
        offsets.Minute(),
        np.timedelta64(4, "h"),
        timedelta(hours=23),
    ]:
        with pytest.raises(IncompatibleFrequency, match=msg):
            p + o
        with pytest.raises(IncompatibleFrequency, match=msg):
            o + p

for freq in ["H", "2H", "3H"]:
    p = Period("2011-04-01 09:00", freq=freq)

    exp = Period("2011-04-03 09:00", freq=freq)
    assert p + offsets.Day(2) == exp
    assert offsets.Day(2) + p == exp

    exp = Period("2011-04-01 12:00", freq=freq)
    assert p + offsets.Hour(3) == exp
    assert offsets.Hour(3) + p == exp

    msg = "cannot use operands with types"
    exp = Period("2011-04-01 12:00", freq=freq)
    assert p + np.timedelta64(3, "h") == exp
    assert np.timedelta64(3, "h") + p == exp

    exp = Period("2011-04-01 10:00", freq=freq)
    assert p + np.timedelta64(3600, "s") == exp
    assert np.timedelta64(3600, "s") + p == exp

    exp = Period("2011-04-01 11:00", freq=freq)
    assert p + timedelta(minutes=120) == exp
    assert timedelta(minutes=120) + p == exp

    exp = Period("2011-04-05 12:00", freq=freq)
    assert p + timedelta(days=4, minutes=180) == exp
    assert timedelta(days=4, minutes=180) + p == exp

    msg = "|".join(
        [
            "Input has different freq",
            "Input cannot be converted to Period",
        ]
    )

    for o in [
        offsets.YearBegin(2),
        offsets.MonthBegin(1),
        offsets.Minute(),
        np.timedelta64(3200, "s"),
        timedelta(hours=23, minutes=30),
    ]:
        with pytest.raises(IncompatibleFrequency, match=msg):
            p + o
        with pytest.raises(IncompatibleFrequency, match=msg):
            o + p
