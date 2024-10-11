# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
other = not_hourly
rng = period_range("2014-01-01 10:00", "2014-01-05 10:00", freq="H")
rng = tm.box_expected(rng, box_with_array)
msg = "|".join(
    [
        # non-timedelta-like DateOffset
        "Input has different freq(=.+)? from Period.*?\\(freq=H\\)",
        # timedelta/td64/Timedelta but not a multiple of 24H
        "Cannot add/subtract timedelta-like from PeriodArray that is "
        "not an integer multiple of the PeriodArray's freq.",
    ]
)

with pytest.raises(IncompatibleFrequency, match=msg):
    rng + other

with pytest.raises(IncompatibleFrequency, match=msg):
    rng += other
