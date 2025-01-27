# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_shift.py
ts = frame_or_series(
    np.random.randn(5), index=date_range("1/1/2000", periods=5, freq="H")
)

result = ts.shift(1, freq="5T")
exp_index = ts.index.shift(1, freq="5T")
tm.assert_index_equal(result.index, exp_index)

# GH#1063, multiple of same base
result = ts.shift(1, freq="4H")
exp_index = ts.index + offsets.Hour(4)
tm.assert_index_equal(result.index, exp_index)
