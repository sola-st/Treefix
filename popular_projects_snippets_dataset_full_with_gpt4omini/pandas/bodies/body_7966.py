# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_constructors.py
msg = "Input has different freq=D from PeriodIndex\\(freq=M\\)"

with pytest.raises(IncompatibleFrequency, match=msg):
    PeriodIndex([Period("2011-01", freq="M"), NaT, Period("2011-01", freq="D")])

with pytest.raises(IncompatibleFrequency, match=msg):
    PeriodIndex(
        np.array(
            [Period("2011-01", freq="M"), NaT, Period("2011-01", freq="D")]
        )
    )

# first element is NaT
with pytest.raises(IncompatibleFrequency, match=msg):
    PeriodIndex([NaT, Period("2011-01", freq="M"), Period("2011-01", freq="D")])

with pytest.raises(IncompatibleFrequency, match=msg):
    PeriodIndex(
        np.array(
            [NaT, Period("2011-01", freq="M"), Period("2011-01", freq="D")]
        )
    )
