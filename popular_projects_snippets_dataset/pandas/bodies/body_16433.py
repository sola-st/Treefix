# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_cut.py
ser = Series([0, 1, 2, 3, 4, 5, 6, 7, 8])
result = cut(ser, 3)

exp_bins = np.linspace(0, 8, num=4).round(3)
exp_bins[0] -= 0.008

expected = Series(
    IntervalIndex.from_breaks(exp_bins, closed="right").take(
        [0, 0, 0, 1, 1, 1, 2, 2, 2]
    )
).astype(CDT(ordered=True))
tm.assert_series_equal(result, expected)
