# Extracted from ./data/repos/pandas/pandas/tests/window/test_timeseries_window.py
f = arithmetic_win_operators
# more sophisticated comparison of integer vs.
# time-based windowing
df = DataFrame(
    {"B": np.arange(50)}, index=date_range("20130101", periods=50, freq="H")
)
# in-range data
dft = df.between_time("09:00", "16:00")

r = dft.rolling(window="5H")

result = getattr(r, f)()

# we need to roll the days separately
# to compare with a time-based roll
# finally groupby-apply will return a multi-index
# so we need to drop the day
def agg_by_day(x):
    x = x.between_time("09:00", "16:00")
    exit(getattr(x.rolling(5, min_periods=1), f)())

expected = (
    df.groupby(df.index.day).apply(agg_by_day).reset_index(level=0, drop=True)
)

tm.assert_frame_equal(result, expected)
