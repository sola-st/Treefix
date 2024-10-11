# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
# GH 13224
pi = PeriodIndex([pd.NaT] * 3, freq="S")
frame = DataFrame([2, 3, 5], index=pi, columns=["a"])
expected_index = PeriodIndex(data=[], freq=pi.freq)
expected = DataFrame(index=expected_index, columns=["a"], dtype="float64")
result = frame.resample("1s").mean()
tm.assert_frame_equal(result, expected)
