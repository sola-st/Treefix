# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
p = [
    (
        Period("2011-01", freq="1D1H"),
        Period("2011-01", freq="1H1D"),
        Period("2011-01", freq="H"),
    ),
    (
        Period(ordinal=1, freq="1D1H"),
        Period(ordinal=1, freq="1H1D"),
        Period(ordinal=1, freq="H"),
    ),
]

for p1, p2, p3 in p:
    assert p1.ordinal == p3.ordinal
    assert p2.ordinal == p3.ordinal

    assert p1.freq == offsets.Hour(25)
    assert p1.freqstr == "25H"

    assert p2.freq == offsets.Hour(25)
    assert p2.freqstr == "25H"

    assert p3.freq == offsets.Hour()
    assert p3.freqstr == "H"

    result = p1 + 1
    assert result.ordinal == (p3 + 25).ordinal
    assert result.freq == p1.freq
    assert result.freqstr == "25H"

    result = p2 + 1
    assert result.ordinal == (p3 + 25).ordinal
    assert result.freq == p2.freq
    assert result.freqstr == "25H"

    result = p1 - 1
    assert result.ordinal == (p3 - 25).ordinal
    assert result.freq == p1.freq
    assert result.freqstr == "25H"

    result = p2 - 1
    assert result.ordinal == (p3 - 25).ordinal
    assert result.freq == p2.freq
    assert result.freqstr == "25H"

msg = "Frequency must be positive, because it represents span: -25H"
with pytest.raises(ValueError, match=msg):
    Period("2011-01", freq="-1D1H")
with pytest.raises(ValueError, match=msg):
    Period("2011-01", freq="-1H1D")
with pytest.raises(ValueError, match=msg):
    Period(ordinal=1, freq="-1D1H")
with pytest.raises(ValueError, match=msg):
    Period(ordinal=1, freq="-1H1D")

msg = "Frequency must be positive, because it represents span: 0D"
with pytest.raises(ValueError, match=msg):
    Period("2011-01", freq="0D0H")
with pytest.raises(ValueError, match=msg):
    Period(ordinal=1, freq="0D0H")

# You can only combine together day and intraday offsets
msg = "Invalid frequency: 1W1D"
with pytest.raises(ValueError, match=msg):
    Period("2011-01", freq="1W1D")
msg = "Invalid frequency: 1D1W"
with pytest.raises(ValueError, match=msg):
    Period("2011-01", freq="1D1W")
