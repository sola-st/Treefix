# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
msg = (
    "Frequency <MonthEnd> cannot be resampled to <Week: weekday=6>, "
    "as they are not sub or super periods"
)
with pytest.raises(IncompatibleFrequency, match=msg):
    Series(
        range(3), index=period_range(start="2000", periods=3, freq="M")
    ).resample("W").mean()
