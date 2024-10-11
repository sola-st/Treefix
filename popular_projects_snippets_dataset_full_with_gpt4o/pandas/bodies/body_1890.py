# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
# These are incompatible period rules for resampling
ts = simple_period_range_series("1/1/1990", "6/30/1995", freq="w-wed")
msg = (
    "Frequency <Week: weekday=2> cannot be resampled to "
    f"{expected_error_msg}, as they are not sub or super periods"
)
with pytest.raises(IncompatibleFrequency, match=msg):
    ts.resample(rule).mean()
