# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
# GH 13224
index = PeriodIndex(periods, freq="S")
frame = DataFrame(values, index=index)

expected_index = period_range(
    "1970-01-01 00:00:00", periods=len(expected_values), freq=freq
)
expected = DataFrame(expected_values, index=expected_index)
result = frame.resample(freq).mean()
tm.assert_frame_equal(result, expected)
