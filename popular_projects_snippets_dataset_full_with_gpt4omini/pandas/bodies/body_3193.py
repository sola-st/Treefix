# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_pct_change.py
# GH#11150
pnl = DataFrame(
    [np.arange(0, 40, 10), np.arange(0, 40, 10), np.arange(0, 40, 10)]
).astype(np.float64)
pnl.iat[1, 0] = np.nan
pnl.iat[1, 1] = np.nan
pnl.iat[2, 3] = 60

for axis in range(2):
    expected = pnl.ffill(axis=axis) / pnl.ffill(axis=axis).shift(axis=axis) - 1
    result = pnl.pct_change(axis=axis, fill_method="pad")

    tm.assert_frame_equal(result, expected)
