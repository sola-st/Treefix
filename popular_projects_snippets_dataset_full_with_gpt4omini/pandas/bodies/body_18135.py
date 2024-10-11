# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
box = box_with_array
xbox = box if box not in [pd.array, tm.to_array] else pd.Index

tdi = TimedeltaIndex(["1 hours", "2 hours"], freq=tdi_freq)
dti = Timestamp("2018-03-07 17:16:40") + tdi
pi = dti.to_period(pi_freq)

# TODO: parametrize over box for pi?
td64obj = tm.box_expected(tdi, box)

if pi_freq == "H":
    result = pi - td64obj
    expected = (pi.to_timestamp("S") - tdi).to_period(pi_freq)
    expected = tm.box_expected(expected, xbox)
    tm.assert_equal(result, expected)

    # Subtract from scalar
    result = pi[0] - td64obj
    expected = (pi[0].to_timestamp("S") - tdi).to_period(pi_freq)
    expected = tm.box_expected(expected, box)
    tm.assert_equal(result, expected)

elif pi_freq == "D":
    # Tick, but non-compatible
    msg = (
        "Cannot add/subtract timedelta-like from PeriodArray that is "
        "not an integer multiple of the PeriodArray's freq."
    )
    with pytest.raises(IncompatibleFrequency, match=msg):
        pi - td64obj

    with pytest.raises(IncompatibleFrequency, match=msg):
        pi[0] - td64obj

else:
    # With non-Tick freq, we could not add timedelta64 array regardless
    #  of what its resolution is
    msg = "Cannot add or subtract timedelta64"
    with pytest.raises(TypeError, match=msg):
        pi - td64obj
    with pytest.raises(TypeError, match=msg):
        pi[0] - td64obj
